#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .unit import Unit
from .complex_unit import ComplexUnit

class AttachedUnits(Model):
	"""Единицы измерения, составляющие составную единицу измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор сопоставления единиц измерения')
	complex_unit = ForeignKeyField(ComplexUnit, help_text = 'Идентификатор составной единицы измерения')
	attached_unit = ForeignKeyField(Unit, help_text = 'Идентификатор сопоставленной единицы измерения')
	code = SmallIntegerField(index = True, help_text = 'Код единицы измерения')
	
	class Meta:
		table_name = 'attached_units'