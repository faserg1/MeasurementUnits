#!/usr/bin/env python3

import cherrypy
from core.auth import AuthControl
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import MethodNotAllowedError

class Auth:
    @cherrypy.expose
    @formattable()
    def login(self):
        def POST():
            body = cherrypy.request.body_readed
            username = body['username']
            password = body['password']
            token, revoke_date = AuthControl.authorize(username, password)
            return {'token': token, 'revoke_date': revoke_date}
        def default():
            raise MethodNotAllowedError({'error_msg': 'Provided method now allowed.'})
        return invoke_by_method([POST], default)
