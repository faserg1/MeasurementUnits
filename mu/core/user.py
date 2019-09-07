#!/usr/bin/env python3

import hashlib, binascii, os
from db.scheme.user import User as UserTable
from utils.error import ConflictError

class UserControl:
    @staticmethod
    def list_users(org_id = None):
        users = []
        users_obj = UserTable.list_users(org_id)
        return [UserControl._convert_user(user_obj) for user_obj in users_obj]

    @staticmethod
    def create_user(username, email, password):
        hashed_password = UserControl._hash_password(password)
        #TODO: [OOKAMI] Check username & email in cluster mode
        if UserTable.username_exists(username):
            raise ConflictError({'error_msg': 'User with this username already exists'})
        if UserTable.email_exists(email):
            raise ConflictError({'error_msg': 'User with this email already exists'})
        UserTable.create(username, email, hashed_password)

    @staticmethod
    def _get_password_static_salt():
        return 'f1f6fc44-0ca3-4a96-8c90-1c41f06a6954';

    @staticmethod
    def _hash_password(password):
        """Hash a password for storing."""
        password += UserControl._get_password_static_salt()
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def _verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        provided_password += UserControl._get_password_static_salt()
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def _convert_user(user_obj):
        return {'id': str(user_obj.id), 'username': user_obj.username,
            'email': user_obj.email}
