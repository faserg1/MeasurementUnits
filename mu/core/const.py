#!/usr/bin/env python3

class EntityLogModifyType:
	CREATE = 0
	MODIFY = 1
	DELETE = 2

class Privacy:
	PUBLIC = 0
	PROTECTED = 1
	PRIVATE = 2

class Role:
	OWNER = 0
	MAINTAINER = 1
	MEMBER = 2

class ClusterNodeType:
	SIBLING = 0
	PARENT = 1
	CHILD = 2

class DataEncoding:
	NONE = 0
	BASE64 = 1
