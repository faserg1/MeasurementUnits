#!/usr/bin/env python3

from .base import migration

from db.scheme.unit import Unit
from db.scheme.unit_ownership_user import UnitOwnershipUser
from db.scheme.unit_ownership_org import UnitOwnershipOrganizaton
from db.scheme.unit_name import UnitName
from db.scheme.unit_relation import UnitRelation
from db.scheme.unit_group import UnitGroup
from db.scheme.unit_type import UnitType
from db.scheme.unit_code import UnitCode
from db.scheme.simple_unit import SimpleUnit
from db.scheme.complex_unit import ComplexUnit
from db.scheme.attached_units import AttachedUnits
from db.scheme.prefix import Prefix
from db.scheme.prefix_name import PrefixName
from db.scheme.prefix_unit import PrefixUnit

@migration('003f2521-48e8-4b27-8954-6240b9765a4b')
class UnitsMigration:
    _tables = [
		Unit,
        UnitOwnershipUser, UnitOwnershipOrganizaton,
        UnitName, UnitCode,
        UnitType, UnitGroup,
        UnitRelation,
		SimpleUnit, ComplexUnit, AttachedUnits,
        Prefix, PrefixName, PrefixUnit
	]

    description = 'Содержит в себе таблицы с единицами измерения'

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
