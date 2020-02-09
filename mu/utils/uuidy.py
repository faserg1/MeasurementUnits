#!/usr/bin/env python3

def uuidy(uuid_key, on_error = None):
    if not uuid_key:
        on_error()
        return
    try:
        uuid_key = uuid.UUID(uuid_key)
        return uuid_key
    except ValueError as e:
        on_error()
        return
