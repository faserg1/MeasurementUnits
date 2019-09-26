#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import MethodNotAllowedError
from core.auth import (AuthMode, authable)
from core.org import OrganizationControl

class Organization(object):
    @cherrypy.expose
    @authable(AuthMode.USER | AuthMode.ORG)
    @formattable()
    def index(self, *args, **kwargs):
        def GET():
            pass
        def POST():
            try:
                with BodyReader() as body:
                    local_name = body['local_name']
            except MultiKeyError as ex:
                paths = ex.get_error_paths()
                keys = {'paths': paths, 'count': len(paths)}
                raise BadRequestError({'error_msg': 'Request body is not full', 'keys': keys})
            return OrganizationControl.create(local_name)
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
