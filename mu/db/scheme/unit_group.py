#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .unit import Unit
from .group import Group

class UnitGroup(Model):
	"""Группы единиц измерения"""
	id = UUIDField(primary_key = True, help_text = '')
	unit = ForeignKeyField(Unit, backref='groups', help_text = 'Идентификатор единицы измерения')
	group = ForeignKeyField(Group, backref='units', help_text = 'Идентификатор группы')
	
	class Meta:
		table_name = 'unit_group'