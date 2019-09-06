#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from core.auth import authable
from core.user import UserControl

class User(object):
    @cherrypy.expose
    @authable()
    @formattable()
    def index(self):
        def GET():
            users = UserControl.list_users()
            # TODO: [OOKAMI] Check for filter parameters
            # TODO: [OOKAMI] Check for rights
            return {'users': users, 'count': len(users)}
        def POST():
            pass
        def default():
            pass
        return invoke_by_method([GET, POST], default)
