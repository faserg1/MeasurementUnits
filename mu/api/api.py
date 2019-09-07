#!/usr/bin/env python3

import cherrypy
from .app import App
from db.database import Database
from utils.error import handle_error

def connect_to_db():
	db = Database.get()
	db.connect()

def close_db():
	db = Database.get()
	db.close()

cherrypy.tree.mount(App(), '/app/mu/api')
cherrypy.engine.subscribe('before_request', connect_to_db)
cherrypy.engine.subscribe('after_request', close_db)

cherrypy.config.update({'request.error_response': handle_error})
cherrypy.config.update({'tools.trailing_slash.on': False})

def serve():
	cherrypy.engine.start()
	cherrypy.engine.block()
