from ..基础接口 import 操作
from ..命令行接口 import 全局配置
from . import 接口 as 实现接口
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C全局配置ev6(全局配置.I全局配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		return 用户.C用户ev6(self, a用户名)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间ev6(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志ev6(self)
	def f模式_接口(self, a接口):
		from ..基础接口 import 接口 as 北向接口
		from ..命令行接口 import 接口 as 南向接口
		if isinstance(a接口, 南向接口.I接口配置):
			if not a接口.m设备 is self.m设备:
				raise ValueError("设备不匹配")
			v模式 = a接口
		else:
			v接口 = 实现接口.f创建接口ev6(a接口)
			if v接口.m接口.m类型 == 北向接口.E类型.e管理:
				v模式 = 实现接口.C管理ev6(self, v接口)
			else:
				v模式 = 实现接口.C接口ev6(self, v接口)
		return v模式
	#服务
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端ev6, None, a操作)
	def f模式_简单网络管理协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理配置ev6(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱配置ev6(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
