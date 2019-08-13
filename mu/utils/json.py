import json
import cherrypy

def jsonable():
	def jsonable_wrapper(func):
		def func_wrapper(*args, **kwargs):
			cherrypy.response.headers['Content-Type'] = 'application/json'
			return json.dumps(func(*args, **kwargs)).encode('utf-8')
		return func_wrapper
	return jsonable_wrapper