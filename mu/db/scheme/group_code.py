#!/usr/bin/env python3

from peewee import UUIDField, CharField, ForeignKeyField
from .model import Model
from .group import Group
from .standard import Standard

class GroupCode(Model):
	"""Коды группы в стандарте"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор кода группы')
	group = ForeignKeyField(Group, backref = 'codes', help_text = 'Идентификатор группы')
	standard = ForeignKeyField(Standard, backref = 'group_codes', help_text = 'Идентификатор стандарта')
	code = CharField(max_length = 64, index = True, null = True, help_text = 'Код, приписанный типу в данном стандарте')
	
	class Meta:
		table_name = 'group_code'