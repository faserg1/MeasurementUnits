#!/usr/bin/env python3

import uuid
from datetime import datetime
from db.repository.unit import UnitRepository
from db.repository.entity_log import LogWriter
from core.auth_helper import get_user_id
from core.const import (EntityLogModifyType, Privacy)

class UnitsControl:
    @staticmethod
    def create_unit():
        date = datetime.utcnow()
        user_id = get_user_id()
        with UnitRepository.atomic() as txn:
            try:
                unit_id = UnitRepository.create_unit()
                UnitRepository.add_ownership_user(user_id, unit_id, Privacy.PRIVATE)
                LogWriter.push_as_user(unit_id, user_id, None, EntityLogModifyType.CREATE, None, None)
                return {'id': str(unit_id)}
            except Exception as ex:
                txn.rollback()
                raise ex

    @staticmethod
    def add_name(unit_id, lang, short, full, desc):
        date = datetime.utcnow()
        if not isinstance(unit_id, uuid.UUID):
            unit_id = uuid.UUID(unit_id)
        with UnitRepository.atomic() as txn:
            try:
                name_id = UnitRepository.add_name(unit_id, lang, short, full, desc)
                LogWriter.push_as_user(name_id, get_user_id(), None, EntityLogModifyType.CREATE, None, None)
                return {'id': str(name_id)}
            except Exception as ex:
                txn.rollback()
                raise ex

    @staticmethod
    def get_units(with_names = False):
        user_id = get_user_id()
        units = UnitRepository.list_for_user(user_id, with_names)
        units_parsed = []
        for unit in units:
            unit_parsed = {
                'id': str(unit.id),
                'maintenance': unit.maintenance
            }
            if unit.maintenance:
                unit_parsed['maintenance_reason'] = unit.maintenance_reason
            if with_names:
                names_parsed = []
                for name in unit.names:
                    name_parsed = {
                        'id': str(name.id),
                        'lang': str(name.lang.id),
                        'full_name': name.short_name,
                        'short_name': name.full_name,
                        'description': name.description
                    }
                    names_parsed.append(name_parsed)
                name_count = len(names_parsed)
                unit_parsed['name_count'] = name_count
                if len(names_parsed):
                    unit_parsed['names'] = names_parsed
            units_parsed.append(unit_parsed)
        return {'units': units_parsed, 'count': len(units_parsed)}
