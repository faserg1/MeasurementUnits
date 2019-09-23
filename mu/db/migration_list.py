#!/usr/bin/env python3

from db.migrations.master import MasterMigration
from db.migrations.system import SystemMigration
from db.migrations.groups import GroupsMigration
from db.migrations.units import UnitsMigration

def get_migration_list():
    return [MasterMigration, SystemMigration, GroupsMigration, UnitsMigration]
