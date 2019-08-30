#!/usr/bin/env python3

from db.migration import Migration
from db.database import Database

class Setup:
	@staticmethod
	def setup():
		print("Connecting to the database")
		Database.init()
		db = Database.get()
		db.connect()
		print("Setting up MeasurementUnits!")
		Migration.updateDatabase()
