# coding=utf-8

# function --- fibs
'''
fibs = [0, 1]
print fibs
num = input('How many numbers do you want:') #注意这里是input,或者是int(raw_input("")),不然会出错
for i in range(num-2):
	fibs.append(fibs[-2] + fibs[-1])
print fibs
'''

# function --- def
def fibs(num):
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result
print fibs(10)
print fibs(15)

# function --- doc
def square(x):
	'caculate the square of the number x.'
	return x*x
print square.func_doc

# function --- parameters
def printMax(a,b):
	if a > b:
		print a, 'is maximum'
	else:
		print b, 'is maximum'
printMax(5,3)

def say(message, times = 2):
	print message * times
say('hello >> ')
say(4)

def func(a, b=5, c=10):
	print 'a is', a, 'and b is', b, 'and c is', c
func(4)

def variableArgs(arg1, arg2 = 'defaultB', *theRest):  #可变长参数
	print 'arg 1:', arg1
	print 'arg 2:', arg2
	for eachXtrArg in theRest:
		print 'another arg:', eachXtrArg
variableArgs('abc')
variableArgs(45,67,8)
variableArgs('abc',123,'xyz',456.7,888)

def dictVarArgs(arg1, arg2 = 'defaultB', **theRest):	# **关键字变量参数(字典)
	print 'arg 1:', arg1
	print 'arg 2:', arg2
	for eachXtrArg in theRest.keys():
		print 'Xtra arg %s : %s' %(eachXtrArg, str(theRest[eachXtrArg]))		
dictVarArgs(1220, 740.0, c = 'gmail')
dictVarArgs(arg2 = 'tales', c = 123, d = 'zoo', arg1 = 'my')
dictVarArgs('one', d = 10, e = 'zoo', girls = ('Jenny', 'Penny'))

def newfoo(arg1, arg2, *t, **d):
    print 'arg1 is :', arg1
    print 'arg2 is :', arg2
    for eacht in t:
        print 'add non-keyword:', eacht
    for eachd in d.keys():
        print "add keyword '%s': %s" %(eachd, d[eachd])
newfoo(10, 20, 30, 40, foo = 50, bar = 60)
newfoo(2,4,*(6,8),**{'jzhou':22,'James':45})
atuple=(7,8,9)
adict={'jzhou':22}
newfoo(1,2,3,x=4,y=5,z=6,*atuple ,**adict)

# function --- variable scope
def scopetest():
	localvar = 66
	print localvar 
scopetest()
#print localvar		# 外部无法访问def定义中的变量

if True:
	a = 3
	print a 
else:
	print 'not equals 3'
print a				# 在外部也是可以访问 if/elif/else try/except/finally for/while中变量

def func(x):
	print 'x is', x 
	x = 2 			# 局部变量
	print 'Changed local x to', x
x=50
func(x)
print x				# 不改变

def func():
	global x 		# 全局变量
	print 'x is', x 
	x = 2 
	print 'Changed local x to', x 
x=50
func()
print x				# 被修改

# function --- lambda匿名函数
Factorial = lambda x: x>1 and x*Factorial(x-1) or 1
print Factorial(6)
max = lambda a,b: a>b and a or b
print max(2,4)

x,y=11,12
print (lambda:x+y)()	#使用默认的x,y
print (lambda x:x+y)(x)	#传的参数是x,y使用默认的12
print (lambda x:x+y)(y)	#传的参数是y,则y替换x

# function --- yield
def gen(n):
	for i in xrange(n):
		yield i
g = gen(5)
print g.next()
print g.next()
for x in g:
	print x
#print g.next()			# StopIteration 迭代已停止

# function --- iter & next
L = [1,2,3,4,5,6,7,8]
I = iter(L)
print I.next()
print I.next()
for x in I:
	print (x),

print
Y = iter(L)
while True:
	try:
		x = next(Y)
	except StopIteration:
		break
	print x**2,
	
print
R = range(3)
I1,I2 = iter(R),iter(R)
print next(I1), next(I2), next(I1)

# function --- enumerate()
string = 'hello'
print enumerate(string)
print list(enumerate(string))
for index,value in enumerate(string):
	print index, value

# function --- filter()
def f(x):
	return x%2!=0 and x%3!=0
print filter(f, range(2,25))

# function --- map()
def cube(x):
    return x**3
print map(cube, range(1,5))
print filter(cube, range(1,5))
print map(lambda x:x*2, [1,2,3,4,[5,6,7]])
print map(None, 'abc', 'xyz123')

# function --- reduce()
print reduce((lambda x,y:x+y), [1,2,3,4,5])
print reduce((lambda x,y:x*y), [1,2,3,4,5])

# function --- zip()
x,y = [1,2,3], [4,5,6]
print zip(x,y)
print list(zip(x,y))
print dict(zip(x,y))
print tuple(zip(x,y))
T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print list(zip(T1, T2, T3))
print tuple(zip(T1, T2, T3))

# function --- type()
print type(12)
print type('hello')
print type(type(42))
print type([].append)

# function --- cmp()
print cmp(1,2)
print cmp(3,3)
print cmp(4,2)
print cmp(0xFF,255)

# function --- transfer type
print float(4)
print complex(2.4,8)
print ord('s')			# 转换为ASCII
print chr(115)			# 转换为字符
print hex(255)			# 16进制表示
print oct(255)			# 8进制表示

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/09/3010546.html