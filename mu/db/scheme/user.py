#!/usr/bin/env python3

from peewee import UUIDField, CharField
from .model import Model

class User(Model):
	"""Пользователь"""
	id = UUIDField(primary_key = True, help_text = '')
	username = CharField(max_length = 512, index = True, help_text = '')
	hashed_password = CharField(max_length = 512, index = True, help_text = '')
	email = CharField(max_length = 512, help_text = '')