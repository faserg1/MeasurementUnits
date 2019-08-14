#!/usr/bin/env python3

from db.scheme.master import MasterDb

class Setup:
	@staticmethod
	def is_first_start():
		return not MasterDb.has_keys()
	
	@staticmethod
	def setup():
		print("Setting up MeasurementUnits!")