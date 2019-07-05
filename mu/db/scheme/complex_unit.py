#!/usr/bin/env python3

from peewee import ForeignKeyField
from .model import Model
from .unit import Unit

class ComplexUnit(Model):
	"""Составная единица измерения"""
	id = ForeignKeyField(Unit, primary_key = True, column_name = 'id', help_text = 'Идентификатор единицы измерения')
	
	class Meta:
		table_name = 'complex_unit'