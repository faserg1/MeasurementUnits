#!/usr/bin/env python3

from peewee import UUIDField, CharField, BigIntegerField
from .model import Model

class Language(Model):
	"""Язык"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор языка')
	name = CharField(help_text = 'Наименование языка на английском')
	own_name = CharField(help_text = 'Наименование языка')

	class Meta:
		table_name = 'lang'
