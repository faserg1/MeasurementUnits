#!/usr/bin/env python3

import cherrypy
from core.auth import AuthControl
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import MethodNotAllowedError
from utils.body_reader import (BodyReader, MultiKeyError)

class Auth:
    @cherrypy.expose
    @formattable()
    def login(self, *args, **kwargs):
        def POST():
            try:
                with BodyReader() as body:
                    username = body['username']
                    password = body['password']
            except MultiKeyError as ex:
                paths = ex.get_error_paths()
                keys = {'paths': paths, 'count': len(paths)}
                raise BadRequestError({'error_msg': 'Request body is not full', 'keys': keys})
            token, revoke_date = AuthControl.authorize(username, password)
            return {'token': token, 'expired_at': revoke_date}
        def default():
            raise MethodNotAllowedError({'error_msg': 'Provided method now allowed.'})
        return invoke_by_method([POST], default)
