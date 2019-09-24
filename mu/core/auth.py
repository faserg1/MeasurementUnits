#!/usr/bin/env python 3

from datetime import datetime
import cherrypy
from core.master import MasterControl
from core.user import UserControl
from core.auth_helper import (get_auth, validate_auth_type, get_master_key, get_token, get_user_id)
from core.config import Config
from db.scheme.token import Token
from utils.error import (BadRequestError, UnauthorizedError, ForbiddenError, NotFoundError)
from utils.time import get_utc_seconds

class AuthControl:
    @staticmethod
    def authorize(username_or_email, password):
        if MasterControl.is_master_mode():
            raise ForbiddenError({'error_msg': 'Server is under maintance'})
        valid, user = UserControl.validate_user(username_or_email, password)
        if not valid:
            raise UnauthorizedError({'error_msg': 'Invalid password'})
        token, revoke_date = Token.create_token(user, Config.get_revoke_in())
        return str(token), get_utc_seconds(revoke_date)

    @staticmethod
    def revoke_token(token_id):
        if not Token.revoke(token_id):
            raise NotFoundError({'error_msg': 'Token not found'})

# TODO: [OOKAMI] It must first check for master key, then on rights for current user
# Request must have Auth header or smth

class AuthMode:
    MASTER = 0x1
    USER = 0x2
    ORG = 0x4
    ALL = MASTER | USER | ORG

def authable(mode = AuthMode.ALL):
    def wrapper(func):
        def handler_wrapper(*args, **kwargs):
            # No need to check auth
            if not mode:
                return func(*args, **kwargs)
            def master_available():
                return mode & AuthMode.MASTER and MasterControl.is_master_mode()
            auth = get_auth()
            if not auth:
                raise UnauthorizedError({'error_msg': 'No Authorization header is present in request'})
            if not validate_auth_type(auth):
                raise BadRequestError({'error_msg': 'Invalid Authorization header'})
            master_available = master_available()
            if master_available and 'Master-Key' in auth:
                if MasterControl.check_key(auth['Master-Key']):
                    return func(*args, **kwargs)
                else:
                    raise ForbiddenError({'error_msg': 'Invalid Master-Key'})
            elif master_available:
                raise ForbiddenError({'error_msg': 'Cannot access resource while node is in master mode'})
            elif 'Token' in auth and ((mode & AuthMode.USER) or (mode & AuthMode.ORG)):
                token = auth['Token']
                if not Token.validate(token):
                    raise ForbiddenError({'error_msg': 'Invalid token or token has been expired'})
                if not (mode & AuthMode.USER):
                    # TODO: [OOKAMI] Validate organization exists
                    pass
            else:
                raise ForbiddenError({'error_msg': 'Permission denied'})
            return func(*args, **kwargs)
        handler_wrapper.__name__ = func.__name__
        handler_wrapper.__doc__ = func.__doc__
        return handler_wrapper
    return wrapper
