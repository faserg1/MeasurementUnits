#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, DoubleField
from .model import Model
from .unit import Unit

class UnitRelation(Model):
    """Отношение единицы измерения. source:target"""
    id = UUIDField(primary_key = True, help_text = 'Идентификатор отношений единиц измерения')
    target = ForeignKeyField(Unit, help_text = 'Единица измерения, к которой применяется отношение')
    source = ForeignKeyField(Unit, help_text = 'Исходная единица измерения')
    relation = DoubleField(help_text = 'Отношение source к target')

    class Meta:
        table_name = 'unit_relation'
