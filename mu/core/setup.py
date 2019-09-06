#!/usr/bin/env python3

from db.migration import Migration
from db.database import Database
from .master import MasterControl

class Setup:
	@staticmethod
	def setup():
		print("Connecting to the database")
		Database.init()
		db = Database.get()
		db.connect()
		print("Setting up MeasurementUnits!")
		Migration.update_database()
		print("...")
		MasterControl.setup()
		db.close()
