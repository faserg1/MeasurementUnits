import json
import cherrypy

def jsonable():
	def jsonable_wrapper(func):
		def func_wrapper(*args, **kwargs):
			response = func(*args, **kwargs)
			if response:
				cherrypy.response.headers['Content-Type'] = 'application/json'
				return json.dumps(response).encode('utf-8')
		return func_wrapper
	return jsonable_wrapper
