#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField
from .model import Model
from .prefix import Prefix
from .complex_unit import ComplexUnit

class PrefixUnit(Model):
    """Привязка единицы измерения к приставке"""
    id = UUIDField(primary_key = True, help_text = 'Идентификатор привязки приставки')
    prefix = ForeignKeyField(Prefix, backref = 'units', help_text = 'Приставка')
    unit = ForeignKeyField(ComplexUnit, backref = 'prefixes', help_text = 'Единица измерения')

    class Meta:
        table_name = 'prefix_unit'
