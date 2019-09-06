#!/usr/bin/env python3

from db.database import Database
from db.scheme.master import Master
from db.scheme.cluster import Cluster
from db.scheme.user import User
from db.scheme.org import Organization
from db.scheme.entity_log import EntityLog
from db.scheme.token import Token
from db.scheme.lang import Language
from db.scheme.lang_code import LanguageCode
from db.scheme.format import Format
from db.scheme.standard import Standard
from db.scheme.standard_name import StandardName
from db.scheme.type import Type
from db.scheme.type_name import TypeName
from db.scheme.type_code import TypeCode
from db.scheme.group import Group
from db.scheme.group_name import GroupName
from db.scheme.group_code import GroupCode
from db.scheme.unit_format import Unit
from db.scheme.unit_name import UnitName
from db.scheme.unit_group import UnitGroup
from db.scheme.unit_type import UnitType
from db.scheme.unit_code import UnitCode
from db.scheme.unit_format import UnitFormat
from db.scheme.simple_unit import SimpleUnit
from db.scheme.complex_unit import ComplexUnit
from db.scheme.attached_units import AttachedUnits
from db.scheme.prefix import Prefix

class DevMigration:
	__db = Database.get()
	__tables = [
		Master, Cluster, User, Organization,
		EntityLog, Token,
		Language, LanguageCode,
		Format, Standard, StandardName,
		Type, TypeName, TypeCode, Group, GroupName, GroupCode,
		Unit, UnitName, UnitCode, UnitFormat, UnitType, UnitGroup,
		SimpleUnit, ComplexUnit, AttachedUnits, Prefix,
	]

	@classmethod
	def up(cls):
		cls.__db.create_tables(cls.__tables)

	@classmethod
	def down(cls):
		cls.__db.drop_tables(cls.__tables)
