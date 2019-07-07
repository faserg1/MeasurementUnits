#!/usr/bin/env python3

from peewee import UUIDField, CharField
class EntityLog(Model):
    id = UUIDField(primary_key = True, help_text = '')

    class Meta:
        table_name = 'entity_log'
