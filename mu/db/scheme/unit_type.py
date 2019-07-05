#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .unit import Unit
from .type import Type

class UnitType(Model):
	"""Типы единиц измерения"""
	id = UUIDField(primary_key = True, help_text = '')
	unit = ForeignKeyField(Unit, backref='types', help_text = 'Идентификатор единицы измерения')
	type = ForeignKeyField(Type, backref='units', help_text = 'Идентификатор типа')
	
	class Meta:
		table_name = 'unit_type'