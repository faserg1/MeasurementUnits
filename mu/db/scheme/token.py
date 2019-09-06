#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, BooleanField, DateTimeField
from .model import Model
from .user import User

class Token(Model):
	"""Выданные токены авторизации"""
	id = UUIDField(primary_key = True, help_text = 'Токен')
	user = ForeignKeyField(User, help_text = 'Пользователь, которому был выдан токен')
	revoked = BooleanField(index = True, help_text = 'Был ли токен отозван')
	authoraize_date = DateTimeField(index = True, help_text = 'Дата создания токена')
	revoke_date = DateTimeField(index = True, help_text = 'Дата отзыва токена')
