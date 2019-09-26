#!/usr/bin/env python3

from db.scheme.lang import Language
from db.scheme.lang_code import LanguageCode
from db.scheme.entity_log import LogWriter
from core.auth_helper import get_master_key
from core.const import EntityLogModifyType

class LanguageControl:
    @staticmethod
    def create(name, own_name):
        id = Language.add_lang(name, own_name)
        LogWriter.push_as_master(id, get_master_key(), EntityLogModifyType.CREATE, None, None)
        return {'id': str(id)}

    @staticmethod
    def get_all(include_codes = False):
        langs = Language.list_all()
        count = len(langs)
        parsed = []
        if count:
            for lang in langs:
                lang_parsed = {'id': str(lang.id), 'name': lang.name, 'own_name': lang.own_name}
                if include_codes:
                    pass
                parsed.append(lang_parsed)
        return {'count': count, 'langs': parsed}

    @staticmethod
    def get_code(lang_id):
        pass