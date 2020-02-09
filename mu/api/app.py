#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.error import (NotFoundError, MethodNotAllowedError)
from .master import Master
from core.master import MasterControl
from .user import User
from .auth import Auth
from .org import Organization
from .lang import Language
from .units import Units

class App(object):
	def __init__(self):
		self.master = Master()
		self.user = User()
		self.auth = Auth()
		self.org = Organization()
		self.units = Units()
		self.lang = Language()

	def _cp_dispatch(self, vpath):
		if len(vpath) == 0:
			return self
		if vpath[0] == 'master':
			vpath.pop(0)
			return self.master
		elif vpath[0] == 'user':
			vpath.pop(0)
			return self.user
		elif vpath[0] == 'auth':
			vpath.pop(0)
			return self.auth
		elif vpath[0] == 'org':
			vpath.pop(0)
			return self.org
		elif vpath[0] == 'lang':
			vpath.pop(0)
			return self.lang
		elif vpath[0] == 'units':
			vpath.pop(0)
			return self.units
		return vpath

	@cherrypy.expose
	@formattable()
	def index(self):
		if cherrypy.request.method != 'GET':
			raise MethodNotAllowedError({'error_msg': 'Only GET allowed in this request'})
		return {'maintenance': MasterControl.is_master_mode(), 'startup': MasterControl.is_first_start()}

	@cherrypy.expose
	@formattable()
	def default(self, *args, **kwargs):
		resource = '/'.join(args)
		raise NotFoundError({'error_msg': 'Requested resource not found.',
			'resource': resource, 'params': kwargs})
