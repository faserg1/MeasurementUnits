#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, SmallIntegerField
from .model import Model
from .unit import Unit
from .org import Organization

class UnitOwnershipOrganizaton(Model):
	"""Права владения на единицу измерения организации"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор права')
	org = ForeignKeyField(Organization, backref = 'ownership_unit', help_text = 'Организация')
	unit = ForeignKeyField(Unit, backref = 'ownership_org', help_text = 'Единица измерения')
	privacy = SmallIntegerField(index = True, help_text = 'Приватность')

	class Meta:
		table_name = 'unit_ownership_org'
