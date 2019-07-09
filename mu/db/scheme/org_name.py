#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField, ForeignKeyField
from .model import Model
from .org import Organization
from .lang import Language

class OrganizationName(Model):
    id = UUIDField(primary_key = True, help_text = '')
    org = ForeignKeyField(Organization, help_text = '')
    lang = ForeignKeyField(Language, help_text = '')
    name = CharField(max_length = 256, help_text = '')
    description = TextField(help_text = '')
