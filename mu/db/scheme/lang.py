#!/usr/bin/env python3

from peewee import UUIDField, CharField, BigIntegerField
from .model import Model

class Language(Model):
	"""Язык наименований"""
	id = UUIDField(primary_key = True, help_text = '')
	name = CharField(help_text = '')
	own_name = CharField(help_text = '')
	code_num = BigIntegerField(null = True, help_text = '')