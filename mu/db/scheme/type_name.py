#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, ForeignKeyField
from .model import Model
from .type import Type
from .lang import Language

class TypeName(Model):
	"""Имя типа единицы измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор наименования типа')
	type = ForeignKeyField(Type, backref = 'names', help_text = 'Идентификатор типа')
	lang = ForeignKeyField(Language, help_text = 'Идентификатор языка')
	short_name = CharField(max_length=32, help_text = 'Краткое наименование типа')
	full_name = CharField(max_length=256, help_text = 'Полное наименование типа')
	description = TextField(help_text = 'Описание типа')
	
	class Meta:
		table_name = 'type_name'