#!/usr/bin/env python3

from db.database import Database
from db.migrations.dev import DevMigration
from core.setup import Setup
from api.api import serve

Database.init()
db = Database.get()
db.connect()

DevMigration.down()
DevMigration.up()

if Setup.is_first_start():
	Setup.setup()

serve()