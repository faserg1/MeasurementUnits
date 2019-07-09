#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model

class OrganizationAccess:
	""" """
	id = UUIDField(primary_key = True, help_text = '')

	class Meta:
		table_name = 'org_access'