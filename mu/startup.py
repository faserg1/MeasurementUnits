#!/usr/bin/env python3

from db.database import Database
from db.migration import DevMigration

Database.init()
db = Database.get()
db.connect()

DevMigration.up()