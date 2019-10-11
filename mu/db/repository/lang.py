#!/usr/bin/env python3

import uuid
from db.scheme.lang import Language
from db.scheme.lang_code import LanguageCode

class LanguageRepository:
    @staticmethod
    def add_lang(name, own_name):
    	id = uuid.uuid4()
    	Language.insert(id = id, name = name, own_name = own_name).execute()
    	return id

    @staticmethod
    def list_all():
    	return Language.select().objects()

    @staticmethod
    def add_code(lang, type, code):
    	id = uuid.uuid4()
    	LanguageCode.insert(id = id, lang = lang, code_type = type, code = code).execute()
    	return id

    @staticmethod
    def atomic():
        return Language.atomic()
