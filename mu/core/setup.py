#!/usr/bin/env python3

from db.migration import Migration

class Setup:
	@staticmethod
	def setup():
		print("Setting up MeasurementUnits!")
		Migration.updateDatabase()