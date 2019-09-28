#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import (BadRequestError, MethodNotAllowedError)
from utils.body_reader import (BodyReader, MultiKeyError)
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
            try:
                with BodyReader() as body:
                    username = body['username']
                    password = body['password']
                    email = body['email']
            except MultiKeyError as ex:
                paths = ex.get_error_paths()
                keys = {'paths': paths, 'count': len(paths)}
                raise BadRequestError({'error_msg': 'Request body is not full', 'keys': keys})
            return UserControl.create_user(username, email, password)
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
