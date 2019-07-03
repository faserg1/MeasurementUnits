#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .format import Format
from .unit import Unit

class UnitFormat(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	unit = ForeignKeyField(Unit, backref = 'unit_formats', help_text = '')
	format = ForeignKeyField(Format, backref = 'unit_formats', help_text = '')
	pattern = CharField(max_length=1024)