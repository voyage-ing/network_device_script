import enum
#===============================================================================
# 读写权限
#===============================================================================
class E读写权限(enum.IntEnum):
	e只读 = 1
	e只写 = 2
	e读写 = 3
def fi含读(a权限):
	if a权限 in E读写权限:
		return bool(a权限 & E读写权限.e只读)
	else:
		return False
def fi含写(a权限):
	if a权限 in E读写权限:
		return bool(a权限 & E读写权限.e只写)
	else:
		return False