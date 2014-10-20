# coding=utf-8
'''
字典(dictionary)是除列表之外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取，这个键可以是数字、字符串甚至元组。映射可以使用任何不可变对象标识元素，最常用的类型是字符串和元组，python唯一内建的映射类型是字典。
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
people ={   # 使用人名作为键的字典，每个人用另一个字典来表示，phone和addr是子字典的键
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
labels={   # 针对电话号码和地址使用的描述性标签会在打印输出的时候用到
    'phone':'phone number',
    'addr':'address'
    }
name=raw_input('Name:')
request=raw_input ("Phone number(p) or address(a)?")  # 查找电话号码还是地址？使用正确的键
if request=='p':key='phone'  # 使用正确的键：
if request=='a':key='addr'
if name in people:  # 如果名字是字典中的有效键才打印信息
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
x = {}	    #未使用clear方法
print y

x={}
y=x
x['key'] = 'value'
print y
x.clear()	#使用clear方法,可以想象x,y是java中的引用
print y

# dictionary --- copy() 返回一个具有相同键值对的新字典（实现的是浅复制，因为值本身相同，而不是副本, 类比Java引用）
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
x['username'] = 'mlh'
x['machines'].remove('bar')
print y
print x
# dictionary --- deepcopy() 深复制（deep copy）,复制它包含所有的值
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
d.update(x) #提供的字典中的项会被添加到旧的字典中，若有相同的键则会进行覆盖
print d

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/04/2991388.html

