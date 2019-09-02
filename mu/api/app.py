#!/usr/bin/env python3

import cherrypy
from utils.json import jsonable
from .master import Master
from .user import User
from .org import Organization

class App(object):
	def __init__(self):
		self.master = Master()
		self.user = User()
		self.org = Organization()

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
		return vpath

	@cherrypy.expose
	@jsonable()
	def index(self):
		return {"luck": True}
