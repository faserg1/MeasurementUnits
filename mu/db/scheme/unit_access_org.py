#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .unit import Unit
from .user import User

class UnitAccessUser(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	unit = ForeignKeyField(Unit, help_text = '')
	user = ForeignKeyField(User, help_text = '')
	
	class Meta:
		table_name = 'unit_access_user'