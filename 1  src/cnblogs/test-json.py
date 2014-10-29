# coding=utf-8
# JSON（JavaScript Object Notation）是一种轻量级的数据交换格式,或者可理解为一种通讯方式，能被WEB所识别和公认的数据类型，是“名称/值”对的集合（A collection of name/value pairs。

# json --- dumps													# 将python类型的数据编码成json类型
import json
pyobj=[[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(pyobj)
print repr(pyobj)
print encodedjson

data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1, sort_keys = True)							# sort_keys参数
d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys = True)
print d1
print d2
print d3
print d1 == d2
print d1 == d3

d1 = json.dumps(data1, sort_keys=True, indent=4)					# indent参数
print d1

print 'DATA:', repr(data1)
print 'repr(data)	:', len(repr(data1))
print 'dumps(data)	:', len(json.dumps(data1))
print 'dumps(data, indent=2)	:', len(json.dumps(data1, indent=4))
print 'dumps(data, seperators)	:', len(json.dumps(data1, separators=(',',':')))	# separators参数

data = {'b':789, 'c':456, (1,2):123}
#print json.dumps(data)												# 将会报错
print json.dumps(data, skipkeys=True)

# json --- loads													# 将json类型的数据解码成python类型
decodejson=json.loads(encodedjson)
print type(decodejson)  											# 查看解码后的数据类型
print decodejson[4]['key1']
print decodejson

# json --- json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8",default=None, sort_keys=False, **kw)      				# 完整参数

# REF-1: http://www.cnblogs.com/zhoujie/archive/2013/06/08/3126657.html
