#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import (BadRequestError, NotFoundError, MethodNotAllowedError)
from core.lang import LanguageControl
from core.auth import (AuthMode, authable)

class Language:
    @cherrypy.expose
    @formattable()
    def default(self, *args, **kwargs):
        @authable(AuthMode.MASTER | AuthMode.USER | AuthMode.ORG)
        def GET():
            if not len(args):
                return LanguageControl.get_all()
            raise NotFoundError({'error_msg': 'Resource not found'})
        @authable(AuthMode.MASTER)
        def POST():
            if not len(args):
                body = cherrypy.request.body_readed
                name = body['name']
                own_name = body['own_name']
                if not len(name) or not len(own_name):
                    raise BadRequestError({'error_msg': 'Cannot create language with empty name',
                        'name': name, 'own_name': own_name})
                return LanguageControl.create(name, own_name)
            raise NotFoundError({'error_msg': 'Resource not found'})
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
