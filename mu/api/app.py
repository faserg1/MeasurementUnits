#!/usr/bin/env python3

import cherrypy
from utils.json import jsonable
from .master import Master


class App(object):
	def __init__(self):
		self.master = Master()

	def _cp_dispatch(self, vpath):
		if len(vpath) == 0:
			return self
		if vpath[0] == 'master':
			vpath.pop(0)
			return self.master
		return vpath

	@cherrypy.expose
	@jsonable()
	def index(self):
		return {"luck": True}
