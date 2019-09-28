#!/usr/bin/env python3

from db.repository.lang import LanguageRepository
from db.repository.entity_log import LogWriter
from core.mapper.lang import LanguageMapper
from core.auth_helper import get_master_key
from core.const import EntityLogModifyType

class LanguageControl:
    @staticmethod
    def create(name, own_name):
        with LanguageRepository.atomic() as txn:
            try:
                id = LanguageRepository.add_lang(name, own_name)
                LogWriter.push_as_master(id, get_master_key(), EntityLogModifyType.CREATE, None, None)
                return {'id': str(id)}
            except Exception as ex:
                txn.rollback()
                raise ex

    @staticmethod
    def get_all(include_codes = False):
        langs = LanguageRepository.list_all()
        langs_mapped = [LanguageMapper.map_lang(lang, include_codes) for lang in langs]
        return {'count': count, 'langs': parsed}

    @staticmethod
    def get_code(lang_id):
        pass
