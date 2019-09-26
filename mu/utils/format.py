import json
import cherrypy
import re

class ResponseFormat:
	JSON = 'json'
	XML = 'xml'

def get_format():
	format = ResponseFormat.JSON
	if 'format' in cherrypy.request.params:
		format = cherrypy.request.params['format']
	if not check_format(format):
		cherrypy.request.params['format'] = RequestFormat.JSON
		raise ValueError('Wrong format')
	return format

def format_as(body, format):
	if format == ResponseFormat.JSON:
		return json.dumps(body).encode('utf-8'), 'application/json'

def format_from(body, format):
	if format == ResponseFormat.JSON:
		return json.loads(body.decode('utf-8'))

def check_format(format):
	if format == ResponseFormat.JSON:
		return True
	return False

def check_body():
	valid_methods = ['POST', 'PUT', 'PATCH']
	return cherrypy.request.body and (
		not hasattr(cherrypy.request, 'body_readed')) and (
		cherrypy.request.method in valid_methods)

def formattable():
	def format_wrapper(func):
		def func_wrapper(*args, **kwargs):
			#Preparing format
			format = get_format()
			#Handling request
			response = func(*args, **kwargs)
			#Formatting request
			if response:
				body, content_type = format_as(response, format)
				cherrypy.response.headers['Content-Type'] = content_type
				return body
			return None
		func_wrapper.__name__ = func.__name__
		func_wrapper.__doc__ = func.__doc__
		return func_wrapper
	return format_wrapper
