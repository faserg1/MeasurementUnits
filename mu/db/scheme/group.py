#!/usr/bin/env python3

from peewee import UUIDField
from .model import Model

class Group(Model):
	"""Именованная группа единиц измерения, тесно связанных между собой"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор группы')
