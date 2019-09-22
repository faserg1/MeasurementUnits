#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from utils.rest import invoke_by_method
from core.master import MasterControl
from core.auth import (AuthMode, authable)
from core.auth_helper import get_master_key

class Master(object):
    @cherrypy.expose
    @formattable()
    @authable(AuthMode.MASTER)
    def index(self):
        def GET():
    	    return {"enabled": MasterControl.is_master_mode()}
        def DELETE():
            master_key = get_master_key()
            return MasterControl.revoke_key(master_key)
            #TODO: [OOKAMI] Revoke master mode
        def default():
            pass
        return invoke_by_method([GET, DELETE], default)

    def _cp_dispatch(self, vpath):
        if len(vpath) == 0:
            return self
        return vpath
