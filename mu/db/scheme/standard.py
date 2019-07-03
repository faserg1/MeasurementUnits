#!/usr/bin/env python3

from peewee import UUIDField
from .model import Model

class Standard(Model):
	"""Стандарт единицы измерения"""
	id = UUIDField(primary_key=True)
	