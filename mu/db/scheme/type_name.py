#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .type import Type
from .lang import Language

class TypeName(Model):
	id = UUIDField(primary_key = True)
	type = ForeignKeyField(Type, backref = 'names', help_text = '')
	lang = ForeignKeyField(Language, help_text = '')
	short_name = CharField(max_length=32, help_text = '')
	full_name = CharField(max_length=256, help_text = '')