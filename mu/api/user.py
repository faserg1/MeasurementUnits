#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from core.auth import authable
from utils.rest import invoke_by_method

class User(object):
    @cherrypy.expose
    @authable()
    @formattable()
    def index(self):
        def GET():
            return {'users': [], 'count': 0}
        def POST():
            pass
        def default():
            pass
        return invoke_by_method([GET, POST], default)
