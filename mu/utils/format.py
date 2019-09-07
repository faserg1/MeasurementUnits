import json
import cherrypy
import re

class ResponseFormat:
	JSON = 'json'
	XML = 'xml'

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

def formattable():
	def format_wrapper(func):
		def func_wrapper(*args, **kwargs):
			#Preparing format
			format = ResponseFormat.JSON
			if 'format' in cherrypy.request.params:
				format = cherrypy.request.params['format']
			if not check_format(format):
				cherrypy.request.params['format'] = RequestFormat.JSON
				raise ValueError('Wrong format')
			#Formatting request body
			if cherrypy.request.body and not hasattr(cherrypy.request, 'body_readed'):
				body = cherrypy.request.body.read()
				cherrypy.request.body_readed = format_from(body, format)
			#Handling request
			response = func(*args, **kwargs)
			#Formatting request
			if response:
				body, content_type = format_as(response, format)
				cherrypy.response.headers['Content-Type'] = content_type
				return body
			return None
		return func_wrapper
	return format_wrapper
