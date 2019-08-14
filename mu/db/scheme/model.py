#!/usr/bin/env python3

from peewee import Model as PeeweeModel

class Model(PeeweeModel):
	"""Базовая модель"""
	
	@classmethod
	def init(cls, db):
		"""Инициализировать модель базой данных"""
		cls.bind(db)
	
	@classmethod
	def atomic(cls):
		return cls._meta.database.atomic()