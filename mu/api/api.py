#!/usr/bin/env python3

import cherrypy
from .app import App

cherrypy.tree.mount(App(), '/app/mu/api')

def serve():
	cherrypy.engine.start()
	cherrypy.engine.block()