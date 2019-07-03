#!/usr/bin/env python3

from peewee import UUIDField, CharField, SmallIntegerField, ForeignKeyField
from .model import Model
from .lang import Language

class LanguageCode(Model):
	id = UUIDField(primary_key = True, help_text = '')
	lang = ForeignKeyField(Language, backref='code', help_text = '')
	code_type = CharField(max_length=16, index=True, help_text = '')
	code_num = SmallIntegerField(null = True, help_text = '')
	code_sym = CharField(null = True, max_length=32, help_text = '')