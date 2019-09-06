#!/usr/bin/env python3

import uuid
from db.database import Database
from db.migration_registry import register_migration

@classmethod
def _get_name(cls):
    return cls.name
@classmethod
def _get_migration_id(cls):
    return cls.migration_id
@classmethod
def _get_description(cls):
    return cls.description

def migration(id, name = None):
    def migration_class_wrapper(cls):
        #Database
        cls.db = Database.get()
        # Fields
        # TODO: [OOKAMI] Check for uuid
        cls.migration_id = id
        if name:
            cls.name = name
        else:
            cls.name = cls.__name__
        if not hasattr(cls, 'description'):
            cls.desription = ''
            print('Migration "' + cls.name + '" has empty description.')
        # Migration methods
        def up(self):
            pass
        def down(self):
            pass
        if not hasattr(cls, 'up'):
            cls.up = up
            print('The ' + cls.name + ' migration has an empty up migration method')
        if not hasattr(cls, 'down'):
            cls.down = down
            print('The ' + cls.name + ' migration has an empty down migration method')
        # Class Methods
        cls.get_name = _get_name
        cls.get_migration_id = _get_migration_id
        cls.get_description = _get_description
        # Registration
        register_migration(cls)
        return cls
    return migration_class_wrapper
