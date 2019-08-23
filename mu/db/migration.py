#!/usr/bin/env python3

from db.scheme.Migration import Migration as MigrationTable

class Migration:
	@staticmethod
	def updateDatabase():
		if not MigrationTable.table_exists():
			MigrationTable.create_table()
		
	def _fetchMigrationList():
		pass