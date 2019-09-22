#!/usr/bin/env python3

from peewee import UUIDField, SmallIntegerField, ForeignKeyField, DateTimeField, TextField
from .model import Model
from .user import User
from .org import Organization
from .master import Master

from datetime import datetime
import uuid

class EntityLog(Model):
	"""Лог системы"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор записи лога')
	entity = UUIDField(index = True, help_text = 'Сущность, с которой производилась операция')
	user = ForeignKeyField(User, null = True, help_text = 'Пользователь, который производил операию')
	org = ForeignKeyField(Organization, null = True, help_text = 'Организация, которая производила операцию')
	master_key = ForeignKeyField(Master, null = True, help_text = 'Мастер-Ключ, под которым была произведена операция')
	mod_type = SmallIntegerField(index = True, help_text = 'Тип операции')
	timestamp = DateTimeField(index = True, help_text = 'Время операции')
	data = TextField(null = True, help_text = 'Допольнительные данные операции в формате JSON строки')
	user_msg = TextField(null = True, help_text = 'Пользовательское сообщение')

	class Meta:
	    table_name = 'entity_log'

class LogWriter:
	@staticmethod
	def push(entity_id, user, org, master_key, mod_type, data, msg):
		if master_key and (user or org):
			raise ValueError('There must be set only one master-key OR user/+org')
		timestamp = datetime.utcnow()
		id = uuid.uuid4()
		with EntityLog.atomic() as txn:
			EntityLog.insert(id = id, entity = entity_id, user = user, org = org,
				master_key = master_key, mod_type = mod_type, timestamp = timestamp,
				data = data, user_msg = msg).execute()

	@staticmethod
	def push_as_master(entity_id, master_key, mod_type, data, msg):
		return LogWriter.push(entity_id, None, None, master_key, mod_type, data, msg)

	@staticmethod
	def push_as_user(entity_id, user, org, mod_type, data, msg):
		return LogWriter.push(entity_id, user, org, None, mod_type,  data, msg)
