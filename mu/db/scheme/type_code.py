#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .type import Type
from .standard import Standard

class TypeCode(Model):
	"""Коды типов в стандарте"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор кода типа')
	type = ForeignKeyField(Type, backref = 'codes', help_text = 'Идентификатор типа')
	standard = ForeignKeyField(Standard, backref = 'type_codes', help_text = 'Идентификатор стандарта')
	code = CharField(max_length = 64, index = True, null = True, help_text = 'Код, приписанный типу в данном стандарте')

	class Meta:
		table_name = 'type_code'