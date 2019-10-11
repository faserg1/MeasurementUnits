#!/usr/bin/env python3

class QueryHelper:
    @staticmethod
    def get_bool(name, kwargs):
        return name in kwargs and (
            kwargs[name].lower() == 'true' or kwargs[name] == '1')

    @staticmethod
    def get_string(name, kwargs):
        if name in kwargs:
            return str(kwargs[name])

    @staticmethod
    def get_int(name, kwargs):
        if name in kwargs:
            return int(kwargs[name])
