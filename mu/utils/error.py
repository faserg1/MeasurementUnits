#!/usr/bin/env python3

import cherrypy
import sys
from utils.format import formattable

class Error(Exception):
    def __init__(self, status, body):
        self.status = status
        self.body = body

    def get_status(self):
        return self.status

    @formattable()
    def get_body(self):
        return self.body

class BadRequestError(Error):
    def __init__(self, body):
        super().__init__(400, body)

class UnauthorizedError(Error):
    def __init__(self, body):
        super().__init__(401, body)

class ForbiddenError(Error):
    def __init__(self, body):
        super().__init__(403, body)

class NotFoundError(Error):
    def __init__(self, body):
        super().__init__(404, body)

def handle_error():
    type, ex, traceback = sys.exc_info()
    if not issubclass(type, Error):
        cherrypy.response.status = 500
        cherrypy.response.body = cherrypy._cperror.format_exc()
        return
    cherrypy.response.status = ex.get_status()
    cherrypy.response.body = ex.get_body()
