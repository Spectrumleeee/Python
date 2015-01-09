params = {'url':'http://baidu.com'}

def get(*arg, **kwargs):
	print arg
	print kwargs
	print kwargs.get("name", "fe")
	
get("a", "b", name="ss", defa="fddf")

class A(object):
	age = 22
	def __init__(self):
		self.name = '1231231221321'
	def method():
		print 'hello'
	
a = A()
a.b = 1	
print getattr(a, "b", "default")