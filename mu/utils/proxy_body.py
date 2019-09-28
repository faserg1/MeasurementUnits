#!/usr/bin/env python3

class ProxyBody:
    def __init__(self, reader, parent, key, value, has_value):
        self._reader = reader
        self._parent = parent
        self._key = key
        self._value = value
        self._has_value = has_value

    def __bool__(self):
        return self._has_value

    def __getitem__(self, key):
        if self._value and key in self._value:
            value = self._value[key]
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
                return value
            return ProxyBody(self._reader, self, key, value, True)
        self._reader._error_paths.append(self._get_path() + '/' + key)
        return ProxyBody(self._reader, self, key, None, False)

    def _get_path(self):
        if self._parent:
            return self._parent._get_path() + '/' + self._key
        else:
            return '/' + self._key
