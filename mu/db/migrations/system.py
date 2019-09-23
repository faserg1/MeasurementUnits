#!/usr/bin/env python3

from .base import migration

from db.scheme.cluster import Cluster
from db.scheme.user import User
from db.scheme.org import Organization
from db.scheme.user_info import UserInfo
from db.scheme.user_org import UserOrganization
from db.scheme.entity_log import EntityLog
from db.scheme.token import Token

@migration('c6cd1eae-d66a-4862-bb58-cf3c3f79162f')
class SystemMigration:
    _tables = [
		Cluster, User, Organization,
        UserInfo, UserOrganization,
		EntityLog, Token
	]

    description = 'Содержит в себе базовые таблицы системы'

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
