#!/usr/bin/env python 3

import cherrypy
from core.master import MasterControl
from utils.error import (UnauthorizedError, ForbiddenError)
# TODO: [OOKAMI] It must first check for master key, then on rights for current user
# Request must have Auth header or smth

class AuthMode:
    MASTER = 0x1
    USER = 0x2
    ORG = 0x4
    ALL = MASTER | USER | ORG

def authable(mode = AuthMode.ALL):
    def wrapper(func):
        def handler_wrapper(*args, **kwargs):
            # No need to check auth
            if not mode:
                return func(*args, **kwargs)
            def master_available():
                return mode & AuthMode.MASTER and MasterControl.is_master_mode()
            def get_auth():
                if 'Authorization' not in cherrypy.request.headers:
                    return
                auth_header = cherrypy.request.headers['Authorization']
                type, value = auth_header.split()
                return {type: value}
            auth = get_auth()
            if not auth:
                raise UnauthorizedError({'error_msg': 'No auth data present in request header'})
            if master_available() and 'Master-Key' in auth:
                if MasterControl.check_key(auth['Master-Key']):
                    return func(*args, **kwargs)
                else:
                    raise ForbiddenError({'error_msg': 'Invalid Master-Key'})
            else:
                raise ForbiddenError({'error_msg': 'Permission denied'})
            return func(*args, **kwargs)
        return handler_wrapper
    return wrapper
