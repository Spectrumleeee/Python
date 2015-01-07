#coding=utf-8

'''
def foo(debug=True):
	if debug:
		print 'in debug mode'
	print 'done'

foo()
foo(False)

# 定义和使用Python类/对象
class FooClass(object):
	"""my very first class: FooClass"""
	version = 0.1
	def __init__(self, nm='spectrumleeee'):
		"""constructor"""
		self.name = nm
		print 'Created a class instance for', nm
	def showname(self):
		"""display instance attribute and class name"""
		print 'Your name is', self.name
		print 'My name is', self.__class__.__name__
	def showver(self):
		"""display class(static) attribute"""
		print self.version
	def addMe2Me(self,x):
		"""apply + operation to argument"""
		return x + x

instance = FooClass()
instance.showname()
print instance.addMe2Me(5)
print instance.addMe2Me('xyz')
foo1 = FooClass('abc')
foo1.showname()
print foo1.__doc__

num = raw_input('Please Enter Your Age:')
print "Your age is %d" % (int(num))


# 从终端输入字符串，并写入到本地文件中 
# makeTextFile.py
def makeTextFile():
	import os
	ls = os.linesep
	print 

	print 'Current Path: %s' % os.getcwd()
	while True:
		fname = raw_input('Please Enter File Name ')
		if os.path.exists(fname):
			print "ERROR: '%s' already exists" % (fname)
		else:
			break

	all = []
	print "\nEnter lines ('.' by itself to quit). \n"

	while True:
		entry = raw_input('> ')
		if entry == '.':
			break
		else:
			all.append(entry)

	fobj = open(fname, 'w')
	fobj.writelines(['%s%s' % (x, ls) for x in all])
	fobj.close()
	print 'DONE!'

# 文件读取和显示
# readTextFile.py
def readTextFile():
	fname = raw_input('Enter filename: ')
	print 

	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print "*** file open error:", e
	else:
		for eachline in fobj:
			print eachline.strip(),
		fobj.close()
def readWriteTextFile(flag):
	if flag == 0:
		readTextFile()
	else:
		makeTextFile()

def testMultiAssigment():
	x,y,z = 1,2,3
	print x,y,z
	z,x,y = y,z,x
	print x,y,z

if __name__ == "__main__":
	readWrite = raw_input("Enter your choice: 0/1 -- read/write ")
	readWriteTextFile(int(readWrite))


# 函数和函数式编程
def foo():
	print 'bar'
rst = foo()
print rst
print type(rst)

def foo_1():
	return ['xyz', 100000, -98.6]
def bar():
	return 'abc', [43, 'python'], 'Guido'
print bar()


from operator import add, sub
from random import randint, choice
from time import *

ops = {'+':add, '-':sub}
while True:
	op = choice('+-')
	print op
	print ops[op]
	sleep(2)


# 装饰器
from time import ctime, sleep

def tsfunc(func):
	def wrappedFunc():
		print '[%s] %s() called' % (ctime(), func.__name__)
		return func()
	return wrappedFunc

@tsfunc
def foo():
	pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()


def convert(func, seq):
	'conv. sequence of numbers to same type'
	return [func(eachNum) for eachNum in seq]
	
myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)


# filter、map、reduce函数
from random import randint as ri
def odd(n):
	return n % 2
allNums = []
for eachNum in range(9):
	allNums.append(ri(1, 99))

print filter(odd, allNums)

print [n for n in [ri(1,99) for i in range(9)] if n%2]

print [x+2 for x in range(6)]
print [x**2 for x in range(6)]

print map(lambda x:x**3, range(6))

# 偏函数 partial
from operator import add, mul
from functools import partial
add1 = partial(add,1)
mul100 = partial(mul, 100)
baseTwo = partial(int, base=3)
print add1(1)
print mul100(50)
print baseTwo('10010')

# 简单GUI类的例子
from functools import partial
import Tkinter
root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', bg='red', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()

# 生成器 generator
def simpleGen(alist):
	while(len(alist) > 0):
		yield alist.pop(0)
mylist = [ n for n in range(10)]
myGen = simpleGen(mylist)
print myGen.next()
print myGen.next()
print myGen.next()

def counter(start_at=0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr
count = counter(5)
print count()
print count()
count2 = counter(100)
print count2()
print count()

def simpleGen():
	yield 1
	yield '2 --> punch!'
myG = simpleGen()
# print myG.next()
# print myG.next()
# print myG.next()

for eachItem in simpleGen():
	print eachItem


def counter(start_at=0):
	count = start_at
	while True:
		val = (yield count)
		print val
		if val is not None:
			count = val
		else:
			count += 1
			
count = counter(5)
print count.next()
print count.next()
print count.next()
count.send(9)
print count.next()

def foo():
	print 'in foo()'
def bar(argfunc):
	argfunc()
bar(foo)

# import module 和 from module import attr区别
import time
time.sleep(5)
from time import sleep
sleep(5)

# importAs函数
def importAs(module):
	return __import__(module)

mt = importAs('time')
mt.sleep(2)
print 'helo'


class Fruit(object):
	'fruit class'
	def __init__(self):
		pass
		
apple = Fruit()
print apple.__doc__
print Fruit.__name__
print Fruit.__doc__

class P(object):
	def __init__(self):
		print 'initialized P'
	def __del__(self):
		print 'deleted P'

class C(P):
	def __init__(self):
		super(C, self).__init__()
		print 'initialized C'
	def __del__(self):
#		super(C, self).__del__()
		print 'deleted C'
c1 = C()
c2 = c1
c3 = c1
#print id(c1), id(c2), id(c3)
#del c1
#del c2
print c1


from operator import *
vec1 = [12, 24]
vec2 = [2, 3, 4]
opvec = (add, sub, mul, div)
for eachOp in opvec:
	for i in vec1:
		for j in vec2:
			print '%s(%d, %d) = %d ' % (eachOp.__name__, i, j, eachOp(i,j))
'''

def dollarized(fValue):
	strValue = str(fValue)
	isNegative = False
	if strValue[0] == '-':
		isNegative = True
		strValue = strValue[1:]
	strMoney = strValue.split('.')
	strTemp = []

	while (len(strMoney[0]) - 1) / 3 :
		strTemp.append(strMoney[0][-3:])
		strMoney[0] = strMoney[0][:-3]
	strTemp.append(strMoney[0])
	strTemp.reverse()
	myDollar = ','.join(strTemp) + '.' + strMoney[1]
	if isNegative:
		myDollar = '-' + myDollar
	#print myDollar
	return myDollar

class MoneyFmt(object):
	def __init__(self, value=0.0):
		self.value = dollarized(value)
	def update(self, value=None):
		self.value = dollarized(value)
	def __repr__(self):
		return repr(self.value)
	def __str__(self):
		val = '$'
		if self.value[0] == '-' :
			val = '-$' + self.value[1:]
		else:
			val += self.value
		return val
	def __nonzero__(self):
		return bool(self.value)

mft = MoneyFmt(-1234567.89)
print mft