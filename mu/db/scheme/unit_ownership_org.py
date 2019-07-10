#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .unit import Unit
from .org import Organization

class UnitOwnershipOrganizaton(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	org = ForeignKeyField(Organization, backref = 'ownership', help_text = '')
	unit = ForeignKeyField(Unit, backref = 'ownership', help_text = '')
	privacy = SmallIntegerField(index = True, help_text = '')

	class Meta:
		table_name = 'unit_ownership_org'
