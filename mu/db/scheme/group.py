#!/usr/bin/env python3

from peewee import UUIDField, BigIntegerField
from .model import Model
from .standard import Standard

class Group(Model):
	"""Именованная группа единиц измерения, тесно связанных между собой"""
	id = UUIDField(primary_key=True, help_text='Идентификатор группы')
	code = BigIntegerField(index=True)