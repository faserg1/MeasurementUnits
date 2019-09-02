#!/usr/bin/env python3

import cherrypy
from .app import App
from db.database import Database

def connect_to_db():
	db = Database.get()
	db.connect()

def close_db():
	db = Database.get()
	db.close()

cherrypy.tree.mount(App(), '/app/mu/api')
cherrypy.engine.subscribe('before_request', connect_to_db)
cherrypy.engine.subscribe('after_request', close_db)

def serve():
	cherrypy.engine.start()
	cherrypy.engine.block()
