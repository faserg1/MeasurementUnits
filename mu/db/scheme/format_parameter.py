#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, CharField
from .model import Model
from .format import Format

class FormatParameter(Model):
    id = UUIDField(primary_key = True, help_text = '')
    format = ForeignKeyField(Format, backref = 'params', help_text = '')
    key = CharField(max_length = 64, index = True, help_text = '')
    value = CharField(max_length = 256, index = True, help_text = '')
