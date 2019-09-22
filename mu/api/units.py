#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import MethodNotAllowedError
from core.auth import (AuthMode, authable)
from core.units import UnitsControl

class Units:
    @cherrypy.expose
    @formattable()
    @authable(AuthMode.USER | AuthMode.ORG)
    def index(self, *args, **kwargs):
        def GET():
            pass
        def POST():
            return UnitsControl.create_unit()
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
