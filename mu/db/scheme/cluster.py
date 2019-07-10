#!/usr/bin/env python3

from peewee import UUIDField, CharField, BooleanField, SmallIntegerFiel, ForeignKeyField
from .model import Model
from .user import User
from .org import Organization

class Cluster(Model):
	""""""
	id = UUIDField(primary_text = '')
	address = CharField(max_length = 256, index = True, help_text = '')
	type = SmallIntegerField(index = True, help_text = '')
	auto = BooleanField(index = True, help_text = '')
	user_owner = ForeignKeyField(User, null = True, backref = 'cluster', help_text = '')
	org_owner = ForeignKeyField(Organization, null = True, backref = 'cluster', help_text = '')