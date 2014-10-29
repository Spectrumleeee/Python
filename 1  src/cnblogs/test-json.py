# coding=utf-8
# JSON��JavaScript Object Notation����һ�������������ݽ�����ʽ,���߿����Ϊһ��ͨѶ��ʽ���ܱ�WEB��ʶ��͹��ϵ��������ͣ��ǡ�����/ֵ���Եļ��ϣ�A collection of name/value pairs��

# json --- dumps													# ��python���͵����ݱ����json����
import json
pyobj=[[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(pyobj)
print repr(pyobj)
print encodedjson

data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1, sort_keys = True)							# sort_keys����
d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys = True)
print d1
print d2
print d3
print d1 == d2
print d1 == d3

d1 = json.dumps(data1, sort_keys=True, indent=4)					# indent����
print d1

print 'DATA:', repr(data1)
print 'repr(data)	:', len(repr(data1))
print 'dumps(data)	:', len(json.dumps(data1))
print 'dumps(data, indent=2)	:', len(json.dumps(data1, indent=4))
print 'dumps(data, seperators)	:', len(json.dumps(data1, separators=(',',':')))	# separators����

data = {'b':789, 'c':456, (1,2):123}
#print json.dumps(data)												# ���ᱨ��
print json.dumps(data, skipkeys=True)

# json --- loads													# ��json���͵����ݽ����python����
decodejson=json.loads(encodedjson)
print type(decodejson)  											# �鿴��������������
print decodejson[4]['key1']
print decodejson

# json --- json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8",default=None, sort_keys=False, **kw)      				# ��������

# REF-1: http://www.cnblogs.com/zhoujie/archive/2013/06/08/3126657.html
