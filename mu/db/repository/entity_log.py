#!/usr/bin/env python3

import uuid
from datetime import datetime
from db.scheme.entity_log import EntityLog

class LogWriter:
	@staticmethod
	def push(entity_id, user, org, master_key, mod_type, data, msg):
		if master_key and (user or org):
			raise ValueError('There must be set only one master-key OR user/+org')
		timestamp = datetime.utcnow()
		id = uuid.uuid4()
		EntityLog.insert(id = id, entity = entity_id, user = user, org = org,
			master_key = master_key, mod_type = mod_type, timestamp = timestamp,
			data = data, user_msg = msg).execute()

	@staticmethod
	def push_as_master(entity_id, master_key, mod_type, data, msg):
		return LogWriter.push(entity_id, None, None, master_key, mod_type, data, msg)

	@staticmethod
	def push_as_user(entity_id, user, org, mod_type, data, msg):
		return LogWriter.push(entity_id, user, org, None, mod_type,  data, msg)

	@staticmethod
	def atomic():
	    return EntityLog.atomic()
