#!/usr/bin/env python3

from db.scheme.master import Master
from uuid import uuid4
from datetime import datetime

class MasterRepository:
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
	def table_exists():
		return Master.table_exists()

	@staticmethod
	def has_keys():
		with Master.atomic() as txn:
			return Master.select().count() > 0

	@staticmethod
	def is_startup():
		with Master.atomic() as txn:
			return Master.select().count() == 1

	@staticmethod
	def is_master_mode():
		if not Master.table_exists():
			print("Master table does not exists!")
			return True
		master_mode = False
		with Master.atomic() as txn:
			now = datetime.utcnow()
			keys = Master.select().where(Master.revoked == False)
			for key in keys:
				if key.revoke_date and key.revoke_date < now:
					key.revoked = True
					key.revoke_date = datetime.utcnow()
					key.save()
				else:
					master_mode = True
		return master_mode

	@staticmethod
	def revoke(id):
		with Master.atomic() as txn:
			try:
				key = Master[id]
				if not key:
					return False
				key.revoked = True
				key.revoke_date = datetime.utcnow()
				key.save()
				return True
			except DoesNotExist as ex:
				return False
