#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.error import NotFoundError
from .master import Master
from .user import User
from .units import Units
from .org import Organization
from .auth import Auth

class App(object):
	def __init__(self):
		self.master = Master()
		self.user = User()
		self.units = Units()
		self.org = Organization()
		self.auth = Auth()

	def _cp_dispatch(self, vpath):
		if len(vpath) == 0:
			return self
		if vpath[0] == 'master':
			vpath.pop(0)
			return self.master
		elif vpath[0] == 'user':
			vpath.pop(0)
			return self.user
		elif vpath[0] == 'org':
			vpath.pop(0)
			return self.org
		elif vpath[0] == 'auth':
			vpath.pop(0)
			return self.auth
		elif vpath[0] == 'units':
			vpath.pop(0)
			return self.units
		return vpath

	@cherrypy.expose
	@formattable()
	def index(self, *args, **kwargs):
		return {"luck": True}

	@cherrypy.expose
	@formattable()
	def default(self, *args, **kwargs):
		resource = '/'.join(args)
		raise NotFoundError({'error_msg': 'Requested resource not found.',
			'resource': resource, 'params': kwargs})
