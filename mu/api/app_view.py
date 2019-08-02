#!/usr/bin/env python3

import inspect
#from .app import app
from utils.class_utils import get_class_of_method
from utils.route_data import RouteData
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
		routes = []
		data_cls = cls._get_data_class()
		if data_cls:
			cls._route = data_cls.route
			routes.append(data_cls.route)
		parents = self._get_recursive_parents()
		for parent in parents:
			data_cls = parent._get_data_class()
			if data_cls:
				cls._route = data_cls.route
				routes.insert(0, data_cls.route)
		self._full_route = "/".join(routes)
	
	@staticmethod
	def route(*args, **kwargs):
		def route_wrapper(func):
			print(cls)
			#cls = get_class_of_method(func)
			func_wrapper = lambda *l_args, **l_kwargs: json.dumps(func(*l_args, **l_kwargs))
			cls._routes.append(RouteData(cls, "", func.__name__, func_wrapper, *args, **kwargs))
			#cls._app.add_url_rule(cls._full_route, func.__name__, func_wrapper, *args, **kwargs)
		return route_wrapper
	
	@classmethod
	def _get_recursive_parents(cls):
		parents = []
		data_cls = cls._get_data_class()
		if data_cls:
			if 'parent' in data_cls.__dict__:
				temp_parent = data_cls.parent
				parent = None
				if inspect.isclass(parent):
					parent = temp_parent
				else:
					parent = temp_parent.__class__
				if parent:
					parents.append(parent)
					parents_inner = parent._get_recursive_parents()
					parents += parents_inner
		return parents
	
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

