#!/usr/bin/env python3

class LanguageMapper:
    @staticmethod
    def map_lang(lang_db, with_codes = True):
        lang_mapped = {
            'id': str(lang_db.id),
            'name': lang_db.name,
            'own_name': lang_db.own_name
        }
        if with_codes:
            pass
        return lang_mapped

    @staticmethod
    def map_lang_code(map_lang_id = True):
        pass
