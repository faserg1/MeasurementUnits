#!/usr/bin/env python3

import copy

_MIGRATION_LIST = []
_MIGRATION_DICT = {}

def register_migration(migration):
    id = migration.get_migration_id()
    name = migration.get_name()
    if id in _MIGRATION_DICT:
        old_cls = _MIGRATION_DICT[id]
        old_name = old_cls.get_name()
        raise ValueError('The "' + name + '" migration has duplicate id "' +
            str(id) + '" with "' + old_name + '"!')
    _MIGRATION_LIST.append(migration)
    _MIGRATION_DICT[id] = migration

def get_all_migrations():
    return copy.copy(_MIGRATION_LIST)

def get_migration_by_id(id):
    return _MIGRATION_DICT[id]
