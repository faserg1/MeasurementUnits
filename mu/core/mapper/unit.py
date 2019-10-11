#!/usr/bin/env python3

class UnitMapper:
    @staticmethod
    def map_unit(unit_db, map_unit_name = True):
        unit_mapped = {
            'id': str(unit_db.id),
            'maintenance': unit_db.maintenance
        }
        if unit_db.maintenance:
            unit_mapped['maintenance_reason'] = unit_db.maintenance_reason
        if map_unit_name:
            names_mapped = [UnitMapper.map_unit_name(name, False) for name in unit_db.names]
            name_count = len(names_mapped)
            unit_mapped['name_count'] = name_count
            if len(names_mapped):
                unit_mapped['names'] = names_mapped
        return unit_mapped

    @staticmethod
    def map_unit_name(unit_db_name, map_unit_id = True):
        name_mapped = {
            'id': str(unit_db_name.id),
            'lang_id': str(unit_db_name.lang.id),
            'full_name': unit_db_name.short_name,
            'short_name': unit_db_name.full_name,
            'description': unit_db_name.description
        }
        if map_unit_id:
            name_mapped['unit_id'] = str(unit_db_name.unit.id)
        return name_mapped
