#!/usr/bin/env python3

from peewee import UUIDField, BooleanField, DateTimeField, DoesNotExist
from .model import Model

class Master(Model):
	"""Модель со значениями корневых прав доступа для узла"""
	id = UUIDField(primary_key = True, help_text = '')
	revoked = BooleanField(index = True, help_text = '')
	authoraize_date = DateTimeField(index = True, help_text = '')
	revoke_date = DateTimeField(index = True, null = True, help_text = '')

from uuid import uuid4
from datetime import datetime

class MasterHelper:
	"""Помощник для управления корневыми правами доступа"""

	@staticmethod
	def check(id):
		with Master.atomic() as txn:
			try:
				key = Master[id]
				if not key:
					return False
				if key.revoked:
					return False
				if key.revoke_date and key.revoke_date < datetime.utcnow():
					key.revoked = True
					key.save()
					return False
				return True
			except DoesNotExist as ex:
				return False

	@staticmethod
	def create():
		with Master.atomic() as txn:
			id = uuid4()
			date = datetime.utcnow()
			q = Master.insert(id = id, revoked = False, authoraize_date = date)
			q.execute()
			return id

	@staticmethod
	def has_keys():
		with Master.atomic() as txn:
			return Master.select().count() > 0

	@staticmethod
	def is_master_mode():
		master_mode = False
		with Master.atomic() as txn:
			now = datetime.utcnow()
			keys = Master.select().where(Master.revoked == False)
			for key in keys:
				if key.revoke_date and key.revoke_date < now:
					key.revoked = True
					key.save()
				else:
					master_mode = True
		return master_mode
