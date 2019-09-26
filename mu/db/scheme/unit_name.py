#!/usr/bin/env python3

import uuid
from peewee import UUIDField, CharField, TextField, ForeignKeyField
from .model import Model
from .unit import Unit
from .lang import Language

class UnitName(Model):
	"""Наименование и описание единицы измерения"""
	id = UUIDField(column_name = 'id', primary_key = True, help_text = 'Идентификатор наименования единицы измерения')
	unit = ForeignKeyField(Unit, backref='names', help_text = 'Идентификатор единицы измерения')
	lang = ForeignKeyField(Language, help_text = 'Идентификатор языка')
	short_name = CharField(max_length = 32, help_text = 'Краткое наименование единицы измерения')
	full_name = CharField(max_length = 256, help_text = 'Полное наименование единицы измерения')
	description = TextField(help_text = 'Описание единицы измерения')

	class Meta:
		table_name = 'unit_name'

	@staticmethod
	def add_name(unit, lang, short, full, desc):
		id = uuid.uuid4()
		with UnitName.atomic() as txn:
			UnitName.insert(id = id, unit = unit, lang = lang,
				short_name = short, full_name = full, description = desc).execute()
			return id
