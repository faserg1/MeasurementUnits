#!/usr/bin/env python3

from .database import Database
from .scheme.lang import Language
from .scheme.lang_code import LanguageCode
from .scheme.format import Format
from .scheme.standard import Standard
from .scheme.standard_name import StandardName
from .scheme.type import Type
from .scheme.type_name import TypeName
from .scheme.group import Group
from .scheme.group_name import GroupName
from .scheme.unit_format import Unit
from .scheme.unit_name import UnitName
from .scheme.unit_format import UnitFormat
from .scheme.simple_unit import SimpleUnit
from .scheme.complex_unit import ComplexUnit
from .scheme.prefix import Prefix

class DevMigration:
	__db = Database.get()
	
	@classmethod
	def up(cls):
		cls.__db.create_tables([Language, LanguageCode,
			Format, Standard, StandardName, Type, TypeName, Group, GroupName,
			Unit, UnitName, UnitFormat, SimpleUnit, ComplexUnit, Prefix])
	
	@classmethod
	def down(cls):
		pass