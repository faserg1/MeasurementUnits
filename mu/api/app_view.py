#!/usr/bin/env python3

import inspect
from .app import app

class AppView:
	_full_route = "/"
	_route = "/"
	_parent = None
	
	def __init__(self):
		self._app = app
		data_cls = self._get_data_class()
		if data_cls:
			self._route = data_cls.route
			self._parent = data_cls.parent
		if self._parent:
			_full_route = AppView._normalize_route(self._parent._full_route + "/" + self._route + "/")
	
	def route(self, func, *args, **kwargs):
		self._app.add_url_rule(self._full_route, func.__name__, func, *args, **kwargs)
	
	@classmethod
	def _get_data_class(cls):
		data = cls.__dict__['Data']
		if inspect.isclass(data)
			return data
	
	@staticmethod
	def _normalize_route(route):
		while route.count("//"):
			route = route.replace("//", "/")
		return route