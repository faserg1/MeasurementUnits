#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .user import User

class Token(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	user = ForeignKeyField(User, help_text = '')