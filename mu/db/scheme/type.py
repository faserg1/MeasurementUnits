#!/usr/bin/env python3

from peewee import UUIDField
from .model import Model

class Type(Model):
	"""Тип единицы измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор типа')