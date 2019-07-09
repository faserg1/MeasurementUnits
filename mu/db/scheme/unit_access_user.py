#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .unit import Unit
from .org import Organization

class UnitAccessOrganization(Model):
	""""""
	id = UUIDField(primary_key = True, help_text = '')
	unit = ForeignKeyField(Unit, help_text = '')
	org = ForeignKeyField(Organization, help_text = '')
	
	class Meta:
		table_name = 'unit_access_org'