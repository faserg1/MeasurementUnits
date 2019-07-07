#!/usr/bin/env python3

from peewee import UUIDField, CharField
from .model import Model

class User(Model):
    id = UUIDField(primary_key = True, help_text = '')
