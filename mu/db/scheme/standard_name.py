#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .standard import Standard
from .lang import Language

class StandardName(Model):
	id = UUIDField(primary_key=True)
	std = ForeignKeyField(Standard, backref='names', help_text='Идентификатор стандарта')
	lang = ForeignKeyField(Language, help_text='')
	short_name = CharField(max_length=32, help_text='')
	full_name = CharField(max_length=256, help_text='')