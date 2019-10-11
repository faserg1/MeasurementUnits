#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .unit import Unit
from .user import User

class UnitOwnershipUser(Model):
	"""Права владения на единицу измерения пользователя"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор права')
	user = ForeignKeyField(User, backref = 'ownership_unit', help_text = 'Идентификатор пользователя владельца')
	unit = ForeignKeyField(Unit, backref = 'ownership_user', help_text = 'Единица измерения')
	privacy = SmallIntegerField(index = True, help_text = 'Приватность')

	class Meta:
		table_name = 'unit_ownership_user'
