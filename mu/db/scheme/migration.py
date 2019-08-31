#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, DateTimeField
from .model import Model
from uuid import uuid4
from datetime import datetime

class Migration(Model):
	"""Модель для сохранения историй миграций"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор выполения миграции')
	migration = UUIDField(index = True, help_text = 'Идентификатор целевой миграции')
	timestamp = DateTimeField(index = True, help_text = 'Время выполнения миграции')
	name = CharField(index = True, max_length = 1024, help_text = 'Наименование миграции')
	description = TextField(help_text = 'Описание миграции')
	reason = TextField(null = True, help_text = 'Описание причины миграции')

	def push(id, name, desc, reason):
		exec_id = uuid4()
		timestamp = datetime.utcnow()
		return Migration.insert(id = exec_id, migration = id, timestamp = timestamp,
			name = name, description = desc, reason = reason)

	class Meta:
		table_name = "migrations_history"
