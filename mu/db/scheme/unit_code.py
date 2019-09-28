#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .unit import Unit
from .standard import Standard

class UnitCode(Model):
	"""Наименование и описание единицы измерения"""
	id = UUIDField(column_name = 'id', primary_key = True, help_text = 'Идентификатор наименования единицы измерения')
	unit = ForeignKeyField(Unit, backref='codes', help_text = 'Идентификатор единицы измерения')
	standard = ForeignKeyField(Standard, backref = 'unit_codes', help_text = 'Идентификатор стандарта')
	code = CharField(max_length = 64, index = True, null = True, help_text = 'Код, приписанный единице измерения в данном стандарте')

	class Meta:
		table_name = 'unit_code'
