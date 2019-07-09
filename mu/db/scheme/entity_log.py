#!/usr/bin/env python3

from peewee import UUIDField, SmallIntegerField, ForeignKeyField, DateTimeField, TextField
from .model import Model
from .user import User
from .org import Organization

class EntityLog(Model):
	""" """
    id = UUIDField(primary_key = True, help_text = '')
	entity = UUIDField(index = True, help_text = '')
	user = ForeignKeyField(User, help_text = '')
	org = ForeignKeyField(Organization, null = True, help_text = '')
	mod_type = SmallIntegerField(index = True, help_text = '')
	timestamp = DateTimeField(index = True, help_text = '')
	data = TextField(help_text = '')
	user_msg = TextField(help_text = '')

    class Meta:
        table_name = 'entity_log'
