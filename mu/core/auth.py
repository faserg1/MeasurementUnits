#!/usr/bin/env python 3

from core.master import MasterControl
# TODO: [OOKAMI] It must first check for master key, then on rights for current user
# Request must have Auth header or smth

def authable():
    def wrapper(func):
        def handler_wrapper(*args, **kwargs):
            return func(*args, **kwargs)
