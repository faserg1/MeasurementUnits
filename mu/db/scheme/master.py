#!/usr/bin/env python3

from peewee import UUIDField, BooleanField, DateTimeField, DoesNotExist
from .model import Model

class Master(Model):
	"""Модель со значениями корневых прав доступа для узла"""
	id = UUIDField(primary_key = True, help_text = '')
	revoked = BooleanField(index = True, help_text = '')
	authoraize_date = DateTimeField(index = True, help_text = '')
	revoke_date = DateTimeField(index = True, null = True, help_text = '')
