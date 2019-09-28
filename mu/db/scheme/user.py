#!/usr/bin/env python3

from peewee import UUIDField, CharField
from .model import Model

class User(Model):
	"""Пользователь"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор пользователя')
	username = CharField(max_length = 512, index = True, help_text = 'Имя пользователя в системе')
	hashed_password = CharField(max_length = 512, index = True, help_text = 'Зашифрованный пароль пользователя')
	email = CharField(max_length = 512, help_text = 'Электронная почта пользователя')
