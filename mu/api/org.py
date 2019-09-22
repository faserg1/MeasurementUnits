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
            local_name = cherrypy.request.body_readed['local_name']
            return OrganizationControl.create(local_name)
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
