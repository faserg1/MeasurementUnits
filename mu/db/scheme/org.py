#!/usr/bin/env python3

import uuid
from peewee import UUIDField, CharField
from .model import Model

class Organization(Model):
	"""Организация"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор организации')
	local_name = CharField(max_length = 256, help_text = 'Локальное наименование организации')

	class Meta:
		table_name = 'org'

	@staticmethod
	def create(local_name):
		id = uuid.uuid4()
		with Organization.atomic() as txn:
			Organization.insert(id = id, local_name = local_name).execute()
			return id
