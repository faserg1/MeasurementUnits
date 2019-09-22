#!/usr/bin/env python3

import uuid
from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .org import Organization
from .user import User

class OrganizationUserAccess(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	org = ForeignKeyField(Organization, help_text = '')
	user = ForeignKeyField(User, help_text = '')
	role = SmallIntegerField(index = True, help_text = '')

	class Meta:
		table_name = 'org_user_access'

	@staticmethod
	def add(org, user, role):
		id = uuid.uuid4()
		OrganizationUserAccess.insert(id = id, org = org, user = user, role = role)
		return id
