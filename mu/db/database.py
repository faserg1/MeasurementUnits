#!/usr/bin/env python3

from peewee import DatabaseProxy, PostgresqlDatabase

class Database:
	"""Инициализатор базы данных"""
	__database_proxy = DatabaseProxy()

	@classmethod
	def init(cls):
		"""Инициализация базы данных"""
		psql_db = PostgresqlDatabase('mu', host = 'localhost', user = 'mu_admin', password = '123456')
		cls.__database_proxy.initialize(psql_db)

	@classmethod
	def upgrade(cls):
		"""Обновление базы данных"""
		pass

	@classmethod
	def get(cls):
		"""Получение прокси базы данных"""
		return cls.__database_proxy
