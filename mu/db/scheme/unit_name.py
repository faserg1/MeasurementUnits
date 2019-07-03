#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, ForeignKeyField
from .model import Model
from .unit import Unit
from .lang import Language

class UnitName(Model):
	id = UUIDField(primary_key = True)
	unit = ForeignKeyField(Unit, backref='names', help_text = '')
	lang = ForeignKeyField(Language, help_text = '')
	short_name = CharField(max_length = 32, help_text = '')
	full_name = CharField(max_length = 256, help_text = '')
	description = TextField(help_text = '')