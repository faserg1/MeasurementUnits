#!/usr/bin/env python3

from peewee import UUIDField, SmallIntegerField, ForeignKeyField, DateTimeField, TextField
from .model import Model
from .user import User
from .org import Organization
from .master import Master

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
