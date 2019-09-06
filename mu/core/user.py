#!/usr/bin/env python3

from db.scheme.user import User as UserTable

class UserControl:
    @staticmethod
    def list_users(org_id = None):
        users = []
        users_obj = UserTable.list_users(org_id)
        for user_obj in users_obj:
            user = {'id': user_obj.id, 'username': user_obj.username,
                'email': username.email}
        return users
