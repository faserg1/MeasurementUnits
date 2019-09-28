#!/usr/bin/env python3

import uuid
from peewee import JOIN
from db.scheme.unit import Unit
from db.scheme.unit_name import UnitName
from db.scheme.unit_ownership_user import UnitOwnershipUser
from db.scheme.unit_ownership_org import UnitOwnershipOrganizaton
from core.const import Privacy

class UnitRepository:
    @staticmethod
    def create_unit():
    	unit_id = uuid.uuid4()
    	Unit.insert(id = unit_id, maintenance = True, maintenance_reason = 'Unit created').execute()
    	return unit_id

    @staticmethod
    def add_ownership_user(user, unit, privacy):
    	id_ownership = uuid.uuid4()
    	UnitOwnershipUser.insert(id = id_ownership, user = user, unit = unit,
    		privacy = privacy).execute()
    	return id_ownership

    @staticmethod
    def add_ownership_org(org, unit, privacy):
    	id_ownership = uuid.uuid4()
    	UnitOwnershipOrganizaton.insert(id = id_ownership, org = org, unit = unit,
    		privacy = privacy).execute()
    	return id_ownership

    @staticmethod
    def add_name(unit, lang, short, full, desc):
    	id = uuid.uuid4()
    	UnitName.insert(id = id, unit = unit, lang = lang,
    		short_name = short, full_name = full, description = desc).execute()
    	return id

    @staticmethod
    def list_for_user(user_id, with_names):
        to_select = [Unit]
        if with_names:
            to_select.append(UnitName)
        q = Unit.select(*to_select)
        if with_names:
            q = q.join(UnitName, JOIN.LEFT_OUTER).switch(Unit)
        q = q.join(UnitOwnershipUser, JOIN.LEFT_OUTER).switch(Unit).join(UnitOwnershipOrganizaton, JOIN.LEFT_OUTER).switch(Unit)
        q = q.where((UnitOwnershipUser.user == user_id) |
            ((UnitOwnershipUser.privacy == Privacy.PUBLIC) & (Unit.maintenance == False)) |
            ((UnitOwnershipOrganizaton.privacy == Privacy.PUBLIC) & (Unit.maintenance == False)))
        return q

    @staticmethod
    def atomic():
        return Unit.atomic()
