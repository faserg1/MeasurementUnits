#!/usr/bin/env python3

from peewee import UUIDField, TextField, ForeignKeyField
from .model import Model
from .lang import Language

class Format(Model):
	"""Формат отображения единицы измерения"""
	id = UUIDField(primary_key = True, help_text = '')
	lang = ForeignKeyField(Language, help_text = '')
	description = TextField(help_text = '')