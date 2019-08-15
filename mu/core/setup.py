#!/usr/bin/env python3

from db.scheme.master import MasterDb

class Setup:
	@staticmethod
	def setup():
		print("Setting up MeasurementUnits!")
		if Setup.is_first_start():
			Setup._first_start_setup()
		Setup._updateDatabase()
	
	@staticmethod
	def is_first_start():
		return not MasterDb.table_exists() or not MasterDb.has_keys()
	
	@staticmethod
	def _first_start_setup():
		pass
	
	@staticmethod
	def _updateDatabase():
		print("Updating database...")
		print(__func__.__name__ + ": stub")