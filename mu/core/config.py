#!usr/bin/env python3

from datetime import timedelta

class Config:
    """Класс для чтения и сохранения конфигурации"""

    @staticmethod
    def get_database_config():
        return {'db_name': 'mu', 'host': 'localhost', 'user': 'mu_admin', 'password': '123456'}

    @staticmethod
    def get_revoke_in():
        return timedelta(days = 15)
