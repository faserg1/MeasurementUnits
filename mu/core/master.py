#!/usr/bin/env python

from db.scheme.master import Master as MasterTable, MasterHelper
from utils.error import BadRequestError
import uuid

class MasterControl:
    @staticmethod
    def setup():
        if not MasterTable.table_exists():
            print("Master table does not exists!")
            return
        if not MasterHelper.has_keys():
            print("First start...")
            key = MasterHelper.create()
            print("Your key: \"" + str(key) + "\"")

    @staticmethod
    def is_master_mode():
        if not MasterTable.table_exists():
            print("Master table does not exists!")
            return True
        return MasterHelper.is_master_mode()

    @staticmethod
    def check_key(key):
        if not key:
            raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
        uuid_key = None
        try:
            uuid_key = uuid.UUID(key)
        except ValueError as e:
            raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
        return MasterHelper.check(uuid_key)


    @staticmethod
    def revoke_key(key):
        if not key:
            raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
        uuid_key = None
        try:
            uuid_key = uuid.UUID(key)
        except ValueError as e:
            raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
        MasterHelper.revoke(uuid_key)
