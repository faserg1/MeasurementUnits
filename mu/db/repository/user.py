#!/usr/bin/env python3

import uuid
from db.scheme.user import User

class UserRepository:
    @staticmethod
    def list_users(org_id = None):
        q = User.select()
        if org_id:
            # TODO: [OOKAMI] Check this
            q = q.where(User.orgs == org_id)
        return q.objects()

    @staticmethod
    def username_exists(username):
    	return User.select().where(User.username == username).count() > 0

    @staticmethod
    def email_exists(email):
    	return User.select().where(User.email == email).count() > 0

    @staticmethod
    def find_user(username_or_email):
    	q = User.select().where((User.username == username_or_email) |
    		(User.email == username_or_email)).limit(1).objects()
    	if not len(q):
    		return None
    	return q[0]

    @staticmethod
    def create_user(username, email, hashed_password):
    	id = uuid.uuid4()
    	User.insert(id = id, username = username,
    		hashed_password = hashed_password, email = email).execute()
    	return id

    @staticmethod
    def atomic():
        return User.atomic()
