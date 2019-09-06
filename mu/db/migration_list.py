#!/usr/bin/env python3

from db.migrations.system import SystemMigration

def get_migration_list():
    return [SystemMigration]
