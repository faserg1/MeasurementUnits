#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from utils.error import (NotFoundError, MethodNotAllowedError)
from core.master import MasterControl
from core.auth import (AuthControl, AuthMode, authable)
from core.auth_helper import (get_master_key, get_token_info)

class Master(object):
    def __init__(self):
        self.token = Master.Token()

    @cherrypy.expose
    @formattable()
    def index(self):
        @authable(AuthMode.MASTER | AuthMode.USER | AuthMode.ORG)
        def GET():
            return {"enabled": MasterControl.is_master_mode()}
        @authable(AuthMode.MASTER)
        def DELETE():
            master_key = get_master_key()
            return MasterControl.revoke_key(master_key)
        def default():
            raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
        return invoke_by_method([GET, DELETE], default)

    def _cp_dispatch(self, vpath):
        if len(vpath) == 0:
            return self
        if vpath[0] == 'token':
            vpath.pop(0)
            return self.token
        return vpath

    class Token:
        @cherrypy.expose
        @formattable()
        @authable(AuthMode.MASTER)
        def default(self, *args, **kwargs):
            def GET():
                if len(args) == 1:
                    token_info = get_token_info(args[0])
                    if token_info:
                        return token_info
                raise NotFoundError({'error_msg': 'Resource not found'})
            def DELETE():
                if len(args) == 1:
                    AuthControl.revoke_token(args[0])
                    return
                raise NotFoundError({'error_msg': 'Resource not found'})
            def default():
                raise MethodNotAllowedError({'error_msg': 'Method not allowed'})
            return invoke_by_method([GET, DELETE], default)
