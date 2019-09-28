#!/usr/bin/env python3

from peewee import TextField, BooleanField, UUIDField, ForeignKeyField
from .model import Model
from .group import Group
from .type import Type

from core.const import Privacy

class Unit(Model):
	"""Единица измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор единицы измерения')
	maintenance = BooleanField(index = True, help_text = 'Находится ли единица измерения в режиме обслуживания')
	maintenance_reason = TextField(null = True, help_text = 'Причина перевода единицы измерения в режим обслуживания')
