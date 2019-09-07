#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from .master import Master
from .user import User
from .org import Organization
from .auth import Auth

class App(object):
	def __init__(self):
		self.master = Master()
		self.user = User()
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
		return vpath

	@cherrypy.expose
	@formattable()
	def index(self):
		return {"luck": True}
