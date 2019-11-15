#!/usr/bin/env python3

import uuid
from peewee import JOIN
from db.scheme.unit import Unit
from db.scheme.unit_name import UnitName
from db.scheme.unit_relation import UnitRelation
from db.scheme.unit_ownership_user import UnitOwnershipUser
from db.scheme.unit_ownership_org import UnitOwnershipOrganizaton
from core.const import Privacy

class UnitRepository:
    #Simple operations

    @staticmethod
    def create_unit():
    	unit_id = uuid.uuid4()
    	Unit.insert(id = unit_id, maintenance = True, maintenance_reason = 'Unit created').execute()
    	return unit_id

    @staticmethod
    def delete_unit(unit_id):
        return Unit.delete().where(User.id == unit_id).execute() > 1

    # Unit types

    # TODO: [OOKAMI]

    # Maintenance

    @staticmethod
    def start_maintenance(unit):
        pass

    @staticmethod
    def stop_maintenance(unit):
        pass

    #Ownership

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

    #Relations

    @staticmethod
    def add_relation(source, target, relation):
        id_relation = uuid.uuid4()
        UnitRelation.insert(id = id_relation, source = source, target = target,
            relation = relation).execute()
        return id_relation

    #Naming

    @staticmethod
    def add_name(unit, lang, short, full, desc):
    	id = uuid.uuid4()
    	UnitName.insert(id = id, unit = unit, lang = lang,
    		short_name = short, full_name = full, description = desc).execute()
    	return id

    #Listing and searching

    @staticmethod
    def list_for_user(user_id, with_names, in_maintenance = 0):
        to_select = [Unit]
        if with_names:
            to_select.append(UnitName)
        q = Unit.select(*to_select)
        if with_names:
            q = q.join(UnitName, JOIN.LEFT_OUTER).switch(Unit)
        q = q.join(UnitOwnershipUser, JOIN.LEFT_OUTER).switch(Unit).join(UnitOwnershipOrganizaton, JOIN.LEFT_OUTER).switch(Unit)
        q = q.where((UnitOwnershipUser.user == user_id) |
            (UnitOwnershipUser.privacy == Privacy.PUBLIC) |
            (UnitOwnershipOrganizaton.privacy == Privacy.PUBLIC))
        if in_maintenance == 0:
            q = q.where(~Unit.maintenance)
        elif in_maintenance != 0:
            q = q.where(Unit.maintenance)
        return q

    @staticmethod
    def search_for_user(user_id, search_query, in_maintenance = 0):
        q = UnitRepository.list_for_user(user_id, True, in_maintenance)
        q = q.where((UnitName.full_name % search_query) | (UnitName.full_name % search_query))
        return q

    @staticmethod
    def atomic():
        return Unit.atomic()
