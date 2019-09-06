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
		reason = 'Updating database'
		current_status = Migration._get_current_status()
		list = get_migration_list()
		list_ids = [m.get_migration_id() for m in list]
		while len(current_status) and len(list_ids):
			if current_status[0] == list_ids[0]:
				current_status.pop(0)
				list.pop(0)
				list_ids.pop(0)
			else:
				break
		if len(current_status):
			while len(current_status):
				m_id = current_status.pop()
				m = get_migration_by_id(m_id)
				Migration._migrate(m, False, reason)
		for migration in list:
			Migration._migrate(migration, True, reason)

	@staticmethod
	def _get_current_status():
		print('Fetching migrations')
		migrations = Migration._fetch_migration_list()
		current_status = []
		for migration in migrations:
			if not migration.up:
				current_status.pop()
			else:
				id = migration.target_migration
				current_status.append(id)
		return current_status

	@staticmethod
	def _migrate(migration_cls, up = True, reason = ''):
		migration = migration_cls()
		id = migration.get_migration_id()
		name = migration.get_name()
		description = migration.get_description()
		migration_direction_str = 'to' if up else 'from'
		print('Migrating ' + migration_direction_str + ' "' + name + '".')
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
