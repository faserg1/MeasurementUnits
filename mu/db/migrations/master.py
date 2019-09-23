#!/usr/bin/env python3

from .base import migration

from db.scheme.master import Master

@migration('7e3402ea-d559-41b8-9309-81fb92915067')
class MasterMigration:
    _tables = [
		Master
	]

    description = 'Содержит в себе мастер таблицу'

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
