#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .org import Organization

class UnitAccessOrganizaton(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	org = ForeignKeyField(Organization, backref = 'access', help_text = '')

	class Meta:
		table_name = 'unit_access_org'
