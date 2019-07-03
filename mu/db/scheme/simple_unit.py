#!/usr/bin/env python3

from peewee import ForeignKeyField, BigIntegerField
from .model import Model
from .unit import Unit

class SimpleUnit(Model):
	id = ForeignKeyField(Unit, primary_key = True, help_text = '')
	code = BigIntegerField(index = True, help_text = '')