#!/usr/bin/env python3

from datetime import datetime
from db.scheme.unit import Unit
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
