#!/usr/bin/env python3

from peewee import UUIDField, CharField, SmallIntegerField, ForeignKeyField
from .model import Model
from .lang import Language

class LanguageCode(Model):
	id = UUIDField(primary_key = True, help_text = 'Идентификатор кода языка')
	lang = ForeignKeyField(Language, backref = 'code', help_text = 'Идентификатор языка')
	code_type = CharField(max_length = 64, index = True, help_text = 'Тип/Стандарт кода')
	code = CharField(null = True, max_length = 256, help_text = 'Код')

	class Meta:
		table_name = 'lang_code'
