#!/usr/bin/env python3

from peewee import UUIDField, CharField
from .model import Model

class Organization(Model):
	"""Организация"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор организации')

	class Meta:
		table_name = 'org'
