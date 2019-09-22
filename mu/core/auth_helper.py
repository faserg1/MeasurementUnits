#!/usr/bin/env python 3

import cherrypy
from db.scheme.token import Token

def get_auth():
    if 'Authorization' not in cherrypy.request.headers:
        return
    auth_header = cherrypy.request.headers['Authorization']
    type, value = auth_header.split()
    return {type: value}

def validate_auth_type(auth):
    if 'Master-Key' in auth:
        return True
    if 'Token' in auth:
        return True
    return False

def get_master_key():
    auth = get_auth()
    if not auth:
        return
    if 'Master-Key' not in auth:
        return
    return auth['Master-Key']

def get_token():
    auth = get_auth()
    if not auth:
        return
    if 'Token' not in auth:
        return
    return auth['Token']

def get_user_id():
    token = get_token()
    if not token:
        return
    return Token.get_user(token).id
