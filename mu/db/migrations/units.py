#!/usr/bin/env python3

from .base import migration

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

@migration('003f2521-48e8-4b27-8954-6240b9765a4b')
class UnitsMigration:
    _tables = [
		Unit, UnitName, UnitCode, UnitFormat, UnitType, UnitGroup,
		SimpleUnit, ComplexUnit, AttachedUnits, Prefix
	]

    description = 'Содержит в себе таблицы с единицами измерения'

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
