#!/usr/bin/env python3

from db.scheme.migration import Migration as MigrationTable
from db.database import Database
from .migration_list import get_migration_list
from .migration_registry import (get_all_migrations, get_migration_by_id)

class Migration:
	@staticmethod
	def update_database():
		if not MigrationTable.table_exists():
			print('Creating migration history table')
			MigrationTable.create_table()
		db = Database.get()
		print('Updating database')
		with db.atomic() as txn:
			Migration._do_update()

	@staticmethod
	def _do_update():
		current_status = Migration._get_current_status()
		list = get_migration_list()
		list_ids = [m.get_migration_id() for m in list]
		while len(current_status):
			# TODO: Remove first elements from all lists, while ids are equals, except the last one
			pass
		if len(current_status):
			# TODO: Downgrade database to transaction in first element in list
			# TODO: Remove the first element in list
			pass
		# TODO: Upgrade database by list
		for migration in list:
			Migration._migrate(migration, True, 'Updating database')

	@staticmethod
	def _get_current_status():
		print('Fetching migrations')
		migrations = Migration._fetch_migration_list()
		current_status = []
		prev_migration_id = None
		for migration in migrations:
			id = migration.migration
			if prev_migration_id == id:
				current_status.pop()
			else:
				current_status.append(id)
		return current_status

	@staticmethod
	def _migrate(migration_cls, up = True, reason = ''):
		migration = migration_cls()
		id = migration.get_migration_id()
		name = migration.get_name()
		description = migration.get_description()
		print('Migrating ' + ('to' if up else 'from') + '.')
		if reason:
			print('Reason: "' + reason + '"')
		else:
			print('Empty reason')
		if up:
			migration.up()
		else:
			migration.down()
		MigrationTable.push(id, name, description, up, reason)

	@staticmethod
	def _fetch_migration_list():
		return MigrationTable.select().objects()
