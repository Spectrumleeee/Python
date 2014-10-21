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





















# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/08/3008300.html

