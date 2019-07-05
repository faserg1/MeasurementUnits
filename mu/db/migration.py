#!/usr/bin/env python3

from .database import Database
from .scheme.lang import Language
from .scheme.lang_code import LanguageCode
from .scheme.format import Format
from .scheme.standard import Standard
from .scheme.standard_name import StandardName
from .scheme.type import Type
from .scheme.type_name import TypeName
from .scheme.type_code import TypeCode
from .scheme.group import Group
from .scheme.group_name import GroupName
from .scheme.group_code import GroupCode
from .scheme.unit_format import Unit
from .scheme.unit_name import UnitName
from .scheme.unit_group import UnitGroup
from .scheme.unit_type import UnitType
from .scheme.unit_code import UnitCode
from .scheme.unit_format import UnitFormat
from .scheme.simple_unit import SimpleUnit
from .scheme.complex_unit import ComplexUnit
from .scheme.attached_units import AttachedUnits
from .scheme.prefix import Prefix

class DevMigration:
	__db = Database.get()
	
	@classmethod
	def up(cls):
		cls.__db.create_tables([Language, LanguageCode,
			Format, Standard, StandardName,
			Type, TypeName, TypeCode, Group, GroupName, GroupCode,
			Unit, UnitName, UnitCode, UnitFormat, UnitType, UnitGroup, 
			SimpleUnit, ComplexUnit, AttachedUnits, Prefix])
	
	@classmethod
	def down(cls):
		cls.__db.drop_tables([Language, LanguageCode,
			Format, Standard, StandardName,
			Type, TypeName, TypeCode, Group, GroupName, GroupCode,
			Unit, UnitName, UnitCode, UnitFormat, UnitType, UnitGroup, 
			SimpleUnit, ComplexUnit, AttachedUnits, Prefix])