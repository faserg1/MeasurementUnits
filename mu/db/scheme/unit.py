#!/usr/bin/env python3

from peewee import CharField, BooleanField, UUIDField, ForeignKeyField
from .model import Model
from .group import Group
from .type import Type

class Unit(Model):
	"""Единица измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор единицы измерения')
