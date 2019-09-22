#!/usr/bin/env python3

from core.auth_helper import get_user_id
from core.const import (EntityLogModifyType, Role)
from db.scheme.org import Organization
from db.scheme.org_user_access import OrganizationUserAccess
from db.scheme.entity_log import LogWriter

class OrganizationControl:
    @staticmethod
    def create(local_name):
        user_owner = get_user_id()
        id = Organization.create(local_name)
        role_id = OrganizationUserAccess.add(id, user_owner, Role.OWNER)
        LogWriter.push_as_user(id, user_owner, None, EntityLogModifyType.CREATE, None, None)
