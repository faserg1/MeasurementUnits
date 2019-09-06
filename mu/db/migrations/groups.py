#!/usr/bin/env python3

from .base import migration

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

@migration('8e72a6f6-8b8b-484c-9a57-8760a20035fb')
class GroupsMigration:
    _tables = [
        Language, LanguageCode,
        Format, Standard, StandardName,
        Type, TypeName, TypeCode, Group, GroupName, GroupCode,
	]

    description = 'Содержит в себе таблицы с языками, форматами, стандартами, типами и группами'

    def up(self):
        self.db.create_tables(self._tables)

    def down(self):
        self.db.drop_tables(self._tables)
