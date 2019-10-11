#!/usr/bin/env python3

from peewee import UUIDField, CharField
from .model import Model

class Organization(Model):
	"""Организация"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор организации')
	local_name = CharField(max_length = 256, help_text = 'Локальное наименование организации')

	class Meta:
		table_name = 'org'
