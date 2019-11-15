#!/usr/bin/env python3

from peewee import UUIDField, ForeignKeyField, CharField, TextField
from .model import Model
from .prefix import Prefix
from .lang import Language

class PrefixName(Model):
    """Наименование приставки"""
    id = UUIDField(primary_key = True, help_text = 'Идентификтор наименования приставки')
    prefix = ForeignKeyField(Prefix, backref = 'names', help_text = 'Приставка')
    lang = ForeignKeyField(Language, help_text = 'Язык наименования приставки')
    short_name = CharField(max_length = 16, help_text = 'Короткое наименование')
    full_name = CharField(max_length = 128, help_text = 'Полное наименование')
    description = TextField(help_text = 'Опиание приставки')

    class Meta:
        table_name = 'prefix_name'
