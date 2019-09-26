#!/usr/bin/env python3

import uuid
from datetime import datetime
from db.scheme.unit import Unit
from db.scheme.unit_name import UnitName
from db.scheme.entity_log import LogWriter
from core.auth_helper import get_user_id
from core.const import EntityLogModifyType

class UnitsControl:
    @staticmethod
    def create_unit():
        date = datetime.utcnow()
        id = Unit.create()
        LogWriter.push_as_user(id, get_user_id(), None, EntityLogModifyType.CREATE, None, None)
        return {'id': str(id)}

    @staticmethod
    def add_name(id, lang, short, full, desc):
        date = datetime.utcnow()
        if not isinstance(id, uuid.UUID):
            id = uuid.UUID(id)
        id_name = UnitName.add_name(id, lang, short, full, desc)
        LogWriter.push_as_user(id_name, get_user_id(), None, EntityLogModifyType.CREATE, None, None)
        return {'id': str(id_name)}
