#!/usr/bin/env python3

import uuid
from peewee import TextField, BooleanField, UUIDField, ForeignKeyField
from .model import Model
from .group import Group
from .type import Type

class Unit(Model):
	"""Единица измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор единицы измерения')
	maintense = BooleanField(index = True, help_text = 'Находится ли единица измерения в режиме обслуживания')
	maintense_reason = TextField(null = True, help_text = 'Причина перевода единицы измерения в режим обслуживания')

	@staticmethod
	def create():
		id = uuid.uuid4()
		with Unit.atomic() as txn:
			Unit.insert(id = id, maintense = True, maintense_reason = 'Unit created').execute()
			return id
