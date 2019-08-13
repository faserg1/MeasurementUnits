#!/usr/bin/env python3

import cherrypy
import json
from utils.json import jsonable

class App(object):
	def __init__(self):
		pass
	
	def _cp_dispatch(self, vpath):
		if len(vpath) == 0:
			return self
		return vpath
	
	@cherrypy.expose
	@jsonable()
	def index(self):
		return {"luck": True}