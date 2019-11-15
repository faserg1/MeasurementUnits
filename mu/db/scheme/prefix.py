#!/usr/bin/env python3

from peewee import UUIDField, CharField, TextField
from .model import Model

class Prefix(Model):
	"""Приставка к единицам измерения"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор приставки')
