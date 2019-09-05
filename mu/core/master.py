#!/usr/bin/env python

from db.scheme.master import Master as MasterTable, MasterHelper
from utils.error import BadRequestError
import uuid

class MasterControl:
    @staticmethod
    def setup():
        if not MasterHelper.has_keys():
            print("First start...")
            key = MasterHelper.create()
            print("Your key: \"" + str(key) + "\"")

    @staticmethod
    def is_master_mode():
        return MasterHelper.is_master_mode()

    @staticmethod
    def check_key(key):
        uuid_key = None
        try:
            uuid_key = uuid.UUID(key)
        except ValueError as e:
            raise BadRequestError({'error_msg': 'Ivalid Master-Key'})
        return MasterHelper.check(uuid_key)
