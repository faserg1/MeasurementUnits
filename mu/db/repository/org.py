#!/usr/bin/env python3

import uuid
from db.scheme.org import Organization
from db.scheme.user_org import UserOrganization

class OrganizationRepository:
    @staticmethod
    def create_organization(local_name):
    	id = uuid.uuid4()
    	Organization.insert(id = id, local_name = local_name).execute()
    	return id

    @staticmethod
    def add_role(org, user, role):
    	id = uuid.uuid4()
    	UserOrganization.insert(id = id, org = org, user = user, role = role).execute()
    	return id

    @staticmethod
    def atomic():
        return Organization.atomic()
