#!usr/bin/env python3

class Config:
    """Класс для чтения и сохранения конфигурации"""

    @staticmethod
    def getDatabaseConfig():
        return {'db_name': 'mu', 'host': 'localhost', 'user': 'mu_admin', 'password': '123456'}
