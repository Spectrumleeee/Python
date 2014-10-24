# coding=utf-8

# statements --- print()
print 'Age',22
age = 22
print "Age %s" % age
name='jason'
greeting='hello,'
print greeting,name
print 'hello,',  #如果在结尾处加上逗号，那么接下来的语句会和前一条语句在同一行打印
print 'world!'

# statements --- import() 
import math as m
print m.sqrt(4)
from math import sqrt as S
print S(4)

# statements --- assignment
seq={'name':'jason','phone':'34223'}
key,value=seq.popitem() #获取popitem方法删除时返回的键值对
print key
print value

x=y=z=2
y=3
x=y
print x

x=2
x+=1
x*=2
print x

str = 'python >> '
str *= 2
print str

# statements --- if elif else
'''
num=input('enter a number:')
if num>0:
    print 'positive number'
elif num<0:
    print 'negative number'
else :
    print 'zero'
raw_input('press any key to exit!')
'''

# statements --- is
x=y=[1,2,3]
z=[1,2,3]
print x==y
print x==z
print x is y
print x is z 

y=[2,4]
print x is not y 
del x[2] 
y[1] = 1
y.reverse()
print x == y 
print x is y

# statements --- in
print name
if 's' in name:
	print 'your name contains the ltter "s"'
else:
	print 'your name doesn\t contains the letter "s" '

# statements --- '< == '
print "alpha" < "beta"
print "Lgp".lower() == "LGP".lower()
print [1,2] < [2,1]
print [2,[1,5]] > [2,[1,4]]

# statements --- assert()
age = -1
#assert 0 < age < 100, 'The age must be realistic' #如果age输入在[0,100]之外，则提示出错

# statements --- 'while for'
x = 1
while x<=100:
	print x 
	x*=2 
	
words = ['this','is','an','egg']
for word in words:
	print word,
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
	print num,
print
d = {'x':1, 'y':2, 'z':3}
for key in d:
	print key, 'corresponds to', d[key]

for key,value in d.items():
	print key, 'corresponds to', value

# statements --- for 并行迭代 && zip()
names = ['gplee','jason','james']
ages = [22,42,45]
for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old'

for name,age in zip(names,ages):
	print name, 'is', age, 'years old'
#注意：这里最好不要用range,因为range函数一次创建整个序列，而xrange一次只创建一个数。当需要迭代一个巨大的序列时，无疑xrange更高效。即此例中，使用xrange,序列只创建前5个数，而使用range则创建10000个，而我们只需要5个
print zip(range(5), xrange(10000)) 

# statements --- sorted() & reversed()
print sorted([4,3,6,8,3])
print sorted('hello,python')
print list(reversed('hello,world!'))
print ''.join(reversed('Hello,world!'))

# statements --- break & continue
print range(99,0,-1)
print range(0,10,2)
from math import sqrt
for n in range(99,0,-1):
	root = sqrt(n)
	if root == int(root):
		print n
		break

print [x*x for x in range(10)]
print [x*x for x in range(10) if x%3 == 0]
print [(x,y) for x in range(3) for y in range(4) ]

result = []
for x in range(3):
	for y in range(3):
		result.append((x,y))
print result

# statements --- pass & del & exec & eval
print 'hello'
pass
print 'world'

x = 1
del x 
#print x #x被删除后，则不存在
x = ['hello', 'world']
y = x
y[1] = 'python'
print x 
del x  #删除x后，y依然存在，因为删除的只是名称，而不是列表本身的值
print y

exec 'a=100'	#用来执行储存在字符串或文件中的Python语句。
print a
exec 'print "hello,world!"'
h=['hello']
w='world'
exec('h.append(w)')
print h

str = "for i in range(0,5) : print i"
c = compile(str, '', 'exec')
exec c

print '2 * 3 = ', eval('2*3')

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/08/3008300.html

