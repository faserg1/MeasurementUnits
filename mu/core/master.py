#!/usr/bin/env python

from db.repository.master import MasterRepository
from utils.error import BadRequestError
from utils.uuidy import uuidy

class MasterControl:
    @staticmethod
    def setup():
        if not MasterRepository.table_exists():
            print("Master table does not exists!")
            return
        if not MasterRepository.has_keys():
            print("First start...")
            key = MasterRepository.create()
            print("Your key: \"" + str(key) + "\"")

    @staticmethod
    def is_first_start():
        return MasterRepository.is_startup()

    @staticmethod
    def is_master_mode():
        return MasterRepository.is_master_mode()

    @staticmethod
    def check_key(key):
        return MasterRepository.check(uuidy(key, MasterRepository.key_error))

    @staticmethod
    def revoke_key(key):
        MasterRepository.revoke(uuidy(key, MasterRepository.key_error))

    @staticmethod
    def key_error():
        raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
