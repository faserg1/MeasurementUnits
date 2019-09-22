#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
#from utils.error import
from core.auth import (AuthMode, authable)
from core.user import UserControl

class User(object):
    @cherrypy.expose
    @authable(AuthMode.MASTER | AuthMode.ORG)
    @formattable()
    def index(self):
        def GET():
            users = UserControl.list_users()
            # TODO: [OOKAMI] Check for filter parameters
            # TODO: [OOKAMI] Check for rights
            return {'users': users, 'count': len(users)}
        def POST():
            body = cherrypy.request.body_readed
            UserControl.create_user(body['username'], body['email'], body['password'])
        def default():
            # TODO: [OOKAMI] Raise method not allowed
            pass
        return invoke_by_method([GET, POST], default)
