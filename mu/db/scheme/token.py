#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, BooleanField, DateTimeField
from .model import Model
from .user import User

class Token(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	user = ForeignKeyField(User, help_text = '')
	revoked = BooleanField(index = True, help_text = '')
	authoraize_date = DateTimeField(index = True, help_text = '')
	revoke_date = DateTimeField(index = True, help_text = '')
