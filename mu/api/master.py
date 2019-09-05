#!/usr/bin/env python3

import cherrypy
from utils.format import formattable
from core.master import MasterControl

class Master(object):
    @cherrypy.expose
    @formattable()
    def index(self):
    	return {"enabled": MasterControl.is_master_mode()}

    def _cp_dispatch(self, vpath):
        if len(vpath) == 0:
            return self
        return vpath
