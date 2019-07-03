#!/usr/bin/env python3

from peewee import CharField, BooleanField, UUIDField, ForeignKeyField
from .model import Model
from .standard import Standard
from .group import Group
from .type import Type

class Unit(Model):
	id = UUIDField(primary_key = True)
	standard = ForeignKeyField(Standard, backref = 'units')
	group = ForeignKeyField(Group, backref = 'units')
	type = ForeignKeyField(Type, backref = 'units')
