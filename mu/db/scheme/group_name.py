#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, ForeignKeyField
from .model import Model
from .group import Group
from .lang import Language

class GroupName(Model):
	"""Наименование о описание группы"""
	id = UUIDField(primary_key = True, help_text = '')
	group = ForeignKeyField(Group, backref = 'names', help_text = 'Идентификатор группы')
	lang = ForeignKeyField(Language, help_text = 'Идентификатор языка, на котором ')
	short_name = CharField(max_length = 32, help_text = 'Краткое наименование группы')
	full_name = CharField(max_length = 256, help_text = 'Полное наименование группы')
	description = TextField(help_text = 'Описание группы')
	
	class Meta:
		table_name = 'group_name'