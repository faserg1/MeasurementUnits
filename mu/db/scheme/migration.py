#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, DateTimeField, BooleanField
from .model import Model
from uuid import uuid4
from datetime import datetime

class Migration(Model):
	"""Модель для сохранения историй миграций"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор выполения миграции')
	from_migration = UUIDField(null = True, index = True, help_text = 'Идентификатор предыдущей миграции')
	target_migration = UUIDField(index = True, help_text = 'Идентификатор целевой миграции')
	up = BooleanField(index = True, help_text = 'Поднималась или опускалась миграция')
	timestamp = DateTimeField(index = True, help_text = 'Время выполнения миграции')
	name = CharField(index = True, max_length = 1024, help_text = 'Наименование миграции')
	description = TextField(help_text = 'Описание миграции')
	reason = TextField(null = True, help_text = 'Описание причины миграции')

	@staticmethod
	def get_current_migration():
		migration = Migration.select().order_by(-Migration.timestamp).limit(1)[0]
		return migration.target_migration

	@staticmethod
	def get_previous_migration(of_migration = None):
		if not of_migration:
			of_migration = Migration.get_current_migration()
		up_migration = Migration.select().where(
			up = True, target_migration = of_migration).order_by(
			-Migration.timestamp).limit(1)[0]
		return up_migration.from_migration

	@staticmethod
	def push(id, name, desc, up, reason):
		exec_id = uuid4()
		timestamp = datetime.utcnow()
		current = Migration.get_current_migration()
		prev = Migration.get_previous_migration()
		m_target = id if up else prev
		m_from = current if up else id
		return Migration.insert(id = exec_id,
			target_migration = m_target, from_migration = m_from,
			timestamp = timestamp, name = name, description = desc, reason = reason)

	class Meta:
		table_name = "migrations_history"
