#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import (BadRequestError, NotFoundError, MethodNotAllowedError)
from utils.body_reader import (BodyReader, MultiKeyError)
from utils.query import QueryHelper
from core.auth import (AuthMode, authable)
from core.units import UnitsControl

class Units:
    @cherrypy.expose
    @formattable()
    @authable(AuthMode.USER | AuthMode.ORG)
    def default(self, *args, **kwargs):
        def GET():
            if not len(args):
                search_query = QueryHelper.get_string('search', kwargs)
                in_maintenance = QueryHelper.get_int('in_maintenance', kwargs)
                if search_query:
                    return UnitsControl.search_units(search_query, in_maintenance)
                with_names = QueryHelper.get_bool('names', kwargs)
                return UnitsControl.get_units(with_names, in_maintenance)
            raise NotFoundError({'error_msg': 'Resource not found'})
        def POST():
            if not len(args):
                return UnitsControl.create_unit()
            if len(args) == 2 and args[1] == 'name':
                id = args[0]
                try:
                    with BodyReader() as body:
                        lang = body['lang']
                        short_name = body['short_name']
                        full_name = body['full_name']
                        desc = body['description']
                except MultiKeyError as ex:
                    paths = ex.get_error_paths()
                    keys = {'paths': paths, 'count': len(paths)}
                    raise BadRequestError({'error_msg': 'Request body is not full', 'keys': keys})
                try:
                    return UnitsControl.add_name(id, lang, short_name, full_name, desc)
                except ValueError as ex:
                    raise BadRequestError({'error_msg': 'Bad request'})
            raise NotFoundError({'error_msg': 'Resource not found'})
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, POST], default)
