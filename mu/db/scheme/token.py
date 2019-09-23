#!/usr/bin/env python3

import uuid
import copy
from datetime import datetime

from peewee import UUIDField, ForeignKeyField, BooleanField, DateTimeField, DoesNotExist
from .model import Model
from .user import User

class Token(Model):
	"""Выданные токены авторизации"""
	id = UUIDField(primary_key = True, help_text = 'Токен')
	user = ForeignKeyField(User, help_text = 'Пользователь, которому был выдан токен')
	revoked = BooleanField(index = True, help_text = 'Был ли токен отозван')
	authoraize_date = DateTimeField(index = True, help_text = 'Дата создания токена')
	revoke_date = DateTimeField(index = True, help_text = 'Дата отзыва токена')

	@staticmethod
	def create_token(user, revoke_in):
		id = uuid.uuid4()
		auth_date = datetime.utcnow()
		revoke_date = auth_date + revoke_in
		Token.insert(id = id, user = user, revoked = False,
			authoraize_date = auth_date, revoke_date = revoke_date).execute()
		return id, revoke_date

	@staticmethod
	def validate(token):
		with Token.atomic() as txn:
			try:
				token_record = Token[token]
				if not token_record:
					return False
				if token_record.revoked:
					return False
				now = datetime.utcnow()
				if token_record.revoke_date < now:
					token_record.revoked = True
					token_record.revoke_date = now
					token_record.save()
				return True
			except DoesNotExist:
				return False

	@staticmethod
	def get_user(token):
		with Token.atomic() as txn:
			try:
				token_record = Token[token]
				if not token_record:
					return
				return token_record.user
			except DoesNotExist:
				return

	@staticmethod
	def get_info(token):
		with Token.atomic() as txn:
			try:
				token_record = Token[token]
				if not token_record:
					return
				return token_record
			except DoesNotExist:
				return

	@staticmethod
	def revoke(token):
		with Token.atomic() as txn:
			try:
				token_record = Token[token]
				if not token_record:
					return False
				token_record.revoked = True
				token_record.revoke_date = datetime.utcnow()
				token_record.save()
				return True
			except DoesNotExist:
				return False
