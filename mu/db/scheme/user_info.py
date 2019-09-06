#!/usr/bin/env python3

from peewee import ForeignKeyField
from .model import Model
from .user import User

class UserInfo(Model):
	"""Информация о пользователе"""
	id = ForeignKeyField(User, primary_key = True, help_text = '')

	class Meta:
		table_name = 'user_info'
