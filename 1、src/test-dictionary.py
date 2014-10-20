# coding=utf-8
'''
�ֵ�(dictionary)�ǳ��б�֮��python֮���������������ݽṹ���͡��б�������Ķ����ϣ��ֵ�������Ķ��󼯺ϡ�����֮����������ڣ��ֵ䵱�е�Ԫ����ͨ��������ȡ�ģ�������ͨ��ƫ�ƴ�ȡ����������������֡��ַ�������Ԫ�顣ӳ�����ʹ���κβ��ɱ�����ʶԪ�أ���õ��������ַ�����Ԫ�飬pythonΨһ�ڽ���ӳ���������ֵ䡣
'''

# create a dictionary
phonebook = {'Jason':'23453','James':'34231','Jzhou':'90798'}
print phonebook['Jason']

items = [('name','Gumby'),('age',42)]
d=dict(items)
print d
print d['name']

d=dict(name='Jason',age=42)
print d

# dictionary --- create
x=[]
x.append('floor')
print x
y={}
y[42]='floor'
print y

# dictionary --- complicated example
'''
people ={   # ʹ��������Ϊ�����ֵ䣬ÿ��������һ���ֵ�����ʾ��phone��addr�����ֵ�ļ�
     'Jason':{
        'phone':'2341',
        'addr':'Foo drive 23'
         },
     'James':{
        'phone':'4564',
        'addr':'Bar street 42'
         },
     'Jzhou':{
        'phone':'4564',
        'addr':'Baz avenue 90'
         }
    }
labels={   # ��Ե绰����͵�ַʹ�õ������Ա�ǩ���ڴ�ӡ�����ʱ���õ�
    'phone':'phone number',
    'addr':'address'
    }
name=raw_input('Name:')
request=raw_input ("Phone number(p) or address(a)?")  # ���ҵ绰���뻹�ǵ�ַ��ʹ����ȷ�ļ�
if request=='p':key='phone'  # ʹ����ȷ�ļ���
if request=='a':key='addr'
if name in people:  # ����������ֵ��е���Ч���Ŵ�ӡ��Ϣ
    print "%s's %s is %s." % (name,labels[key],people[name][key])
raw_input("press any key to exit!")
'''

# dictionary --- format
print "Jzhou's phone number is %(Jzhou)s." % phonebook
template = '''<html><head><title>%(title)s</title></head>
<body>
<h1>%(title)s<h1>
<p>%(text)s</p>
</body>'''
data = {'title':'my home page','text':'Welcome to my home age!'}
print template % data

# dictionary --- clear()
d={}
d['name'] = 'Jason'
d['age'] = 42
print d
result = d.clear()
print result

x={}
y=x
x['key'] = 'value'
print y
x = {}	    #δʹ��clear����
print y

x={}
y=x
x['key'] = 'value'
print y
x.clear()	#ʹ��clear����,��������x,y��java�е�����
print y

# dictionary --- copy() ����һ��������ͬ��ֵ�Ե����ֵ䣨ʵ�ֵ���ǳ���ƣ���Ϊֵ������ͬ�������Ǹ���, ���Java���ã�
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
x['username'] = 'mlh'
x['machines'].remove('bar')
print y
print x
# dictionary --- deepcopy() ��ƣ�deep copy��,�������������е�ֵ
from copy import deepcopy
d={}
d['names'] = ['James','Jason']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Jzhou')
print c
print dc

# dictionary --- fromkeys()
result = {}.fromkeys(['name','age'])
print result 
result = dict.fromkeys(['name','sex','age'])
print result
result = dict.fromkeys(['name','age'],'Unknown')
print result

# dictionary --- get()
d={}
#print d['name'] 
print d.get('name')
print d.get('name','N/A')
d['name'] = 'Eric'
print d.get('name')

# dictionary --- has_key()
d={}
print d.has_key('name')
d['name']='Jzhou'
print d.has_key('name')

# dictionary --- keys()
d={'title':'python','url':'http://www.python.org'}
print d.keys()
print d.values()

# dictionary --- pop(), popitem()
d={'x':1,'y':2}
print d.pop('x')
print d

d={'title':'python','url':'http://www.python.org','spam':0}
print d
print d.popitem()
print d.popitem()
print d

# dictionary --- update()
d={
    'title':'Python web site',
    'url':'http://www.python.org',
    'changed':'April 4 20:18 2013'
    }
x={'title':'Python Language Website'}
d.update(x) #�ṩ���ֵ��е���ᱻ��ӵ��ɵ��ֵ��У�������ͬ�ļ������и���
print d

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/04/2991388.html

