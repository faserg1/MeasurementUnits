#!/usr/bin/env python3

from core.auth_helper import get_user_id
from core.const import (EntityLogModifyType, Role)
from db.repository.org import OrganizationRepository
from db.repository.entity_log import LogWriter

class OrganizationControl:
    @staticmethod
    def create(local_name):
        user_owner = get_user_id()
        with OrganizationRepository.atomic() as txn:
            try:
                id = OrganizationRepository.create_organization(local_name)
                role_id = OrganizationRepository.add_role(id, user_owner, Role.OWNER)
                LogWriter.push_as_user(id, user_owner, None, EntityLogModifyType.CREATE, None, None)
                return {'id': str(id), 'role_id': str(role_id)}
            except Exception as ex:
                rxn.rollback()
                raise ex
