#!/usr/bin/env python3

import inspect
#from .app import app
from utils.class_utils import get_class_of_method
import json

class AppView:
	_full_route = "/"
	_route = "/"
	_parent = None
	_routes = []
	
	def __init__(self):
		self.init_self_route()
		self.init_routes()

	@classmethod
	def _init(cls):
		#cls._app = app
		data_cls = cls._get_data_class()
		if data_cls:
			cls._route = data_cls.route
			if 'parent' in data_cls.__dict__:
				cls._parent = data_cls.parent
		if cls._parent:
			_full_route = AppView._normalize_route(cls._parent._full_route + "/" + cls._route + "/")
		else:
			_full_route = AppView._normalize_route(cls._route + "/")
			
	def init_self_route(self):
		data_cls = self._get_data_class()
		if data_cls:
			self._route = data_cls.route
			if 'parent' in data_cls.__dict__:
				parent = data_cls.parent
				if inspect.isclass(parent):
					self._parent = parent
				else:
					self._parent = parent.__class__
		if self._parent:
			pass
	
	@staticmethod
	def route(func, *args, **kwargs):
		cls = get_class_of_method(func)
		func_wrapper = lambda: json.dumps(func())
		cls._app.add_url_rule(cls._full_route, func.__name__, func_wrapper, *args, **kwargs)
	
	@classmethod
	def _get_data_class(cls):
		data = cls.__dict__['Data']
		if inspect.isclass(data):
			return data
	
	@staticmethod
	def _normalize_route(route):
		while route.count("//"):
			route = route.replace("//", "/")
		return route

