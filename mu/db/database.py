#!/usr/bin/env python3

from peewee import DatabaseProxy, PostgresqlDatabase
from core.config import Config

class Database:
	"""Инициализатор базы данных"""
	__database_proxy = DatabaseProxy()

	@classmethod
	def init(cls):
		"""Инициализация базы данных"""
		cfg = Config.getDatabaseConfig()
		db_name = cfg.pop('db_name', "mu")
		psql_db = PostgresqlDatabase(db_name, **cfg)
		cls.__database_proxy.initialize(psql_db)

	@classmethod
	def upgrade(cls):
		"""Обновление базы данных"""
		pass

	@classmethod
	def get(cls):
		"""Получение прокси базы данных"""
		return cls.__database_proxy
