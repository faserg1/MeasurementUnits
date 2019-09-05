import json
import cherrypy
import re

class ResponseFormat:
	JSON = 'json'
	XML = 'xml'

def format_as(body, format):
	if format == ResponseFormat.JSON:
		return json.dumps(body).encode('utf-8'), 'application/json'
	else:
		raise ValueError('Wrong format')

def formattable():
	def format_wrapper(func):
		def func_wrapper(*args, **kwargs):
			response = func(*args, **kwargs)
			if response:
				format = ResponseFormat.JSON
				if 'format' in cherrypy.request.params:
					format = cherrypy.request.params['format']
				try:
					body, content_type = format_as(response, format)
				except ValueError as e:
					cherrypy.request.params['format'] = RequestFormat.JSON
					raise e
				cherrypy.response.headers['Content-Type'] = content_type
				return body
			return None
		return func_wrapper
	return format_wrapper
