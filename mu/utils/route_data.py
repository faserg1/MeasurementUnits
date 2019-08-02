#!/usr/bin/env python3

class RouteData:
	method = ""
	name = ""
	func = None
	args = None
	kwargs = None
	
	def __init__(self, method, name, func, *args, **kwargs):
		self.method = method
		self.name = name
		self.func = func
		self.args = args
		self.kwargs = kwargs