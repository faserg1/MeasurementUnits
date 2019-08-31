#!/usr/bin/env python3

from db.scheme.migration import Migration as MigrationTable
from db.database import Database
from db.migrations.dev import DevMigration

class Migration:
	@staticmethod
	def updateDatabase():
		if not MigrationTable.table_exists():
			MigrationTable.create_table()
		print("Fetching migrations")
		migrations = Migration._fetchMigrationList()
		# TODO: Migration mechanism
		db = Database.get()
		print("Updating database")
		with db.atomic() as txn:
			if len(migrations):
				DevMigration.down()
				MigrationTable.delete().execute()
			DevMigration.up()
			MigrationTable.push('00000000-0000-0000-0000-000000000000',
				'DevMigration', '', '').execute()

	@staticmethod
	def _fetchMigrationList():
		db = Database.get()
		with db.atomic() as txn:
			return MigrationTable.select().objects()
