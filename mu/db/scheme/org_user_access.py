#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .org import Organization
from .user import User

class OrganizationUserAccess(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	org = ForeignKeyField(Organization, help_text = '')
	user = ForeignKeyField(User, help_text = '')
	
	class Meta:
		table_name = 'org_user_access'