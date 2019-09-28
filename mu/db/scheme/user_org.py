#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .org import Organization
from .user import User

class UserOrganization(Model):
	"""Принадлженость пользователей к организациям"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор связи (роли)')
	org = ForeignKeyField(Organization, backref = 'users', help_text = 'Идентификатор организации')
	user = ForeignKeyField(User, backref = 'orgs', help_text = 'Идентификатор пользователя')
	role = SmallIntegerField(index = True, help_text = 'Роль пользователя в организации')

	class Meta:
		table_name = 'user_org'
