#!/usr/bin/env python3

import uuid
from peewee import UUIDField, CharField, BigIntegerField
from .model import Model

class Language(Model):
	"""Язык"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор языка')
	name = CharField(help_text = 'Наименование языка на английском')
	own_name = CharField(help_text = 'Наименование языка')

	class Meta:
		table_name = 'lang'

	@staticmethod
	def add_lang(name, own_name):
		id = uuid.uuid4()
		with Language.atomic() as txn:
			Language.insert(id = id, name = name, own_name = own_name).execute()
			return id

	@staticmethod
	def list_all():
		with Language.atomic() as txn:
			return Language.select().objects()
