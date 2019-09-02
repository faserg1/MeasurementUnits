#!/usr/bin/env python3

import cherrypy
from utils.json import jsonable
from utils.rest import invoke_by_method

class Organization(object):
    @cherrypy.expose
    @jsonable()
    def index(self):
        def GET():
            pass
        def POST():
            pass
        def default():
            pass
        return invoke_by_method([GET, POST], default)
