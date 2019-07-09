#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .org import Organization
from .user import User

class UserOrganization(Model):
	""" """
	id = UUIDField(primary_key = True, help_text = '')
	org = ForeignKeyField(Organization, backref = 'users', help_text = '')
	user = ForeignKeyField(User, backref = 'orgs', help_text = '')

	class Meta:
		table_name = 'user_org'
