#!/usr/bin/env python

from db.scheme.master import Master as MasterTable, MasterHelper

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
