#!/usr/bin/env python3

import copy
import cherrypy
from .format import (check_body, format_from, get_format)
from .proxy_body import ProxyBody

class MultiKeyError(Exception):
    _error_paths = []

    def __init__(self, msg, error_paths):
        super().__init__(self, msg)
        self._error_paths = copy.deepcopy(error_paths)

    def get_error_paths(self):
        return copy.deepcopy(self._error_paths)

class BodyReader:
    _body = None
    _error_paths = []

    def __enter__(self):
        if check_body():
            format = get_format()
            self._body = format_from(cherrypy.request.body.read(), format)
        return self

    def __contains__(self, item):
            return item in self._body

    def __getitem__(self, key):
        if self._body and key in self._body:
            value = self._body[key]
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
                return value
            return ProxyBody(self, None, key, value, True)
        self._error_paths.append('/' + key)
        return ProxyBody(self, None, key, None, False)

    def __exit__(self, type, value, traceback):
        if len(self._error_paths):
            raise MultiKeyError('There is one or more keys not found', self._error_paths)
