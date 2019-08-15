#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, DateTimeField
from .model import Model

class Migration(Model):
	"""Модель для сохранения историй миграций"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор выполения миграции')
	migration = UUIDField(index = True, help_text = 'Идентификатор целевой миграции')
	timestamp = DateTimeField(index = True, help_text = 'Время выполнения миграции')
	name = CharField(max_length = 1024, help_text = 'Наименование миграции')
	description = TextField(help_text = 'Описание миграции')
	reason = TextField(null = True, help_text = 'Описание причины миграции')

	class Meta:
		table_name = "migrations_history"