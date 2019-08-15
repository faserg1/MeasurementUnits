#!/usr/bin/env python3

from peewee import UUIDField, CharField, BooleanField, SmallIntegerField, ForeignKeyField
from .model import Model
from .user import User
from .org import Organization

class Cluster(Model):
	"""Список всех знакомых узлов в кластере"""
	id = UUIDField(primary_key = True, help_text = 'Идентификатор узла')
	address = CharField(max_length = 256, index = True, help_text = 'Адрес узла')
	type = SmallIntegerField(index = True, help_text = 'Тип узла')
	auto = BooleanField(index = True, help_text = 'Тип "знакомства" с узлом')
	user_owner = ForeignKeyField(User, null = True, backref = 'cluster', help_text = 'Владелец узла')
	org_owner = ForeignKeyField(Organization, null = True, backref = 'cluster', help_text = 'Организация, владеющая узлом')