#!/usr/bin/env python3

from db.migrations.system import SystemMigration
from db.migrations.groups import GroupsMigration

def get_migration_list():
    return [SystemMigration, GroupsMigration]
