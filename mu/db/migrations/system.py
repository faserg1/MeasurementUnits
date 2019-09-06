#!/usr/bin/env python3

from .base import migration
import uuid
from db.scheme.master import Master
from db.scheme.cluster import Cluster
from db.scheme.user import User
from db.scheme.org import Organization
from db.scheme.entity_log import EntityLog
from db.scheme.token import Token

@migration('c6cd1eae-d66a-4862-bb58-cf3c3f79162f')
class SystemMigration:
    _tables = [
		Master, Cluster, User, Organization,
		EntityLog, Token
	]

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
