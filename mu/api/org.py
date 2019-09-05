#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method

class Organization(object):
    @cherrypy.expose
    @formattable()
    def index(self):
        def GET():
            pass
        def POST():
            pass
        def default():
            pass
        return invoke_by_method([GET, POST], default)
