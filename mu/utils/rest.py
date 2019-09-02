#!/usr/bin/env python3

import cherrypy

def invoke_by_method(funcs, default, *args, **kwargs):
    if not funcs or not len(funcs):
        raise ValueError("There must be valid funcs")
    funcs_dict = {func.__name__: func for func in funcs}
    if cherrypy.request.method == 'OPTIONS':
        cherrypy.response.headers['Allow'] = ', '.join(funcs_dict.keys())
        return
    if cherrypy.request.method in funcs_dict:
        return funcs_dict[cherrypy.request.method](*args, **kwargs)
    return default(*args, **kwargs)
