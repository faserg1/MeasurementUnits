#!/usr/bin/env python3

from peewee import UUIDField, TextField
from .model import Model

class Format(Model):
	"""Формат отображения единицы измерения"""
	id = UUIDField(primary_key = True, help_text = '')
	description = TextField(help_text = '')
