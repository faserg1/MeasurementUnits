#!/usr/bin/env python3

import uuid
from peewee import UUIDField, CharField
from .model import Model

class User(Model):
	"""Пользователь"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор пользователя')
	username = CharField(max_length = 512, index = True, help_text = 'Имя пользователя в системе')
	hashed_password = CharField(max_length = 512, index = True, help_text = 'Зашифрованный пароль пользователя')
	email = CharField(max_length = 512, help_text = 'Электронная почта пользователя')

	@staticmethod
	def list_users(org_id = None):
		q = User.select()
		if org_id:
			q = q.where(User.orgs == org_id)
		return q.objects()

	@staticmethod
	def username_exists(username):
		return User.select().where(User.username == username).count()

	@staticmethod
	def email_exists(email):
		return User.select().where(User.email == email).count()

	@staticmethod
	def find_user(username_or_email):
		q = User.select().where((User.username == username_or_email) |
			(User.email == username_or_email)).limit(1).objects()
		if not len(q):
			return None
		return q[0]

	@staticmethod
	def create(username, email, hashed_password):
		id = uuid.uuid4()
		User.insert(id = id, username = username,
			hashed_password = hashed_password, email = email).execute()
