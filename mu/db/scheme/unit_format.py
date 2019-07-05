#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .format import Format
from .unit import Unit

class UnitFormat(Model):
	"""Форматированная единица измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор формата единицы измерения')
	unit = ForeignKeyField(Unit, backref = 'unit_formats', help_text = 'Идентификатор единицы измерения')
	format = ForeignKeyField(Format, backref = 'unit_formats', help_text = 'Формат, в котором записана эта единица измерения')
	pattern = CharField(max_length=1024, help_text = 'Шаблон, по которому нужно записать единицу измерения')
	
	class Meta:
		table_name = 'unit_format'