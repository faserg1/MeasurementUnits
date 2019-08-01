#!/usr/bin/env python3

from app_ver import AppVer0_1

class Master0_1(AppVer0_1):
	
	@route()
	def hello():
		return {}
	
	class Data:
		route = "master"