#!/usr/bin/env python3

import hashlib, binascii, os
from datetime import datetime
from db.scheme.user import User as UserTable
from db.scheme.entity_log import LogWriter
from core.auth_helper import get_master_key
from core.const import EntityLogModifyType
from utils.error import (NotFoundError, ConflictError, InternalServerError)

class UserControl:
    @staticmethod
    def list_users(org_id = None):
        users = []
        users_obj = UserTable.list_users(org_id)
        return [UserControl._convert_user(user_obj) for user_obj in users_obj]

    @staticmethod
    def create_user(username, email, password):
        date = datetime.utcnow()
        hashed_password = UserControl._hash_password(password)
        #TODO: [OOKAMI] Check username & email in cluster mode
        if UserTable.username_exists(username):
            raise ConflictError({'error_msg': 'User with this username already exists'})
        if UserTable.email_exists(email):
            raise ConflictError({'error_msg': 'User with this email already exists'})
        master_key = get_master_key()
        if not master_key:
            raise InternalServerError({'error_msg': 'Non master key usage creating is not implemented right now'})
        id = UserTable.create(username, email, hashed_password)
        LogWriter.push_as_master(id, master_key, EntityLogModifyType.CREATE, None, None)

    @staticmethod
    def validate_user(username_or_email, password):
        user = UserTable.find_user(username_or_email)
        if not user:
            raise NotFoundError({'error_msg': 'User with provided username or email has not been found.'})
        return UserControl._verify_password(user.hashed_password, password), user

    @staticmethod
    def _get_password_static_salt():
        #NOTE: [OOKAMI] Maybe expose in some setting
        return 'f1f6fc44-0ca3-4a96-8c90-1c41f06a6954';

    @staticmethod
    def _hash_password(password):
        """Hash a password for storing."""
        static_salt = UserControl._get_password_static_salt()
        password += static_salt
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                    salt + static_salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def _verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        static_salt = UserControl._get_password_static_salt()
        provided_password += static_salt
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii') + static_salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def _convert_user(user_obj):
        return {'id': str(user_obj.id), 'username': user_obj.username,
            'email': user_obj.email}
