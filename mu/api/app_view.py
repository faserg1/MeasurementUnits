#!/usr/bin/env python3

class AppView:
	_base_route = "/"
	_app = None
	
	def __init__(self, app, route, parent):
		self._app = app
		if parent:
			_base_route = AppView.normalize_route(parent._base_route + "/" + route + "/")
	
	def route(self, func, *args, **kwargs):
		self._app.add_url_rule(self._base_route, func.__name__, func, *args, **kwargs)
	
	@staticmethod
	def normalize_route(route):
		while route.count("//"):
			route = route.replace("//", "/")
		return route