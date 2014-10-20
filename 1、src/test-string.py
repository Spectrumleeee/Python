# coding=utf-8

# String --- format
'''
width=input('Please input width:')
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format ='%-*s%*.2f'
print '=' * width
print header_format % (item_width,'Item',price_width ,'Price')
print '-' * width
print format % (item_width ,'Apples',price_width ,0.4)
print format % (item_width ,'Pears',price_width ,0.5)
print format % (item_width ,'Cantaloupes',price_width ,1.92)
print format % (item_width ,'Dried Apricots(16 oz.)',price_width ,8)
print format % (item_width ,'Prunes(4 lbs.)',price_width ,12)
print '=' * width
raw_input("enter any key to exit~~")
'''

# String --- find()
print "hello,python,I like python".find('python')
print "hahha,hekko,hello".find('find')
print "$$$ Get rich now !!!$$$".find('$$$')
print "$$$ Get rich now !!!$$$".find('$$$',1)
print "$$$ Get rich now !!!$$$".find('$$$',0,10)

# String --- join()
digitals=['1','2','3','4','5']
seperaor='+'
result = seperaor.join(digitals)
print result
dir='','usr','bin','env'
result = '/'.join(dir)
print result
result = 'C:'+'\\'.join(dir)
print result

# String --- lower()
result = 'Trouble Is a Friend!'.lower()
print result
name = 'Jzhou'
names = ['jason','james','jzhou']
if name in names:  #未转换时没有匹配
    print 'Found it first!'
if name.lower() in names:   #将转换为小写进行匹配
    print 'Found it twice!'

# String --- title()、string.capwords()
result = 'i like python!'.title()
print result
import string
result = string.capwords("i like python!")
print result

# String --- replace()
result = 'this is a test!'.replace('test','work').title()
print result

# String --- split()
print '1+*+2+_+3+-+4+-+5'.split('+')
print '/usr/bin/env'.split('/')
print 'Using the default'.split ()

# String --- strip()
print '      internal whtiespace is kept    '.strip ()
print '****!!SPAM** for ** everyone!!*******'.strip('*!').lower().title()

# String --- maketrans()、translate()
from string import maketrans
table = maketrans('cs','kz') #就是把table中的字符c换成k,字符s换成z
print len(table)
print table[97:123]
print maketrans('','')[97:123]
print 'this is an incredibele test'.translate(table)
print 'Hen,fuck is not a good word'.translate(table,'fuck') #translate的第二个参数是可选的，这个参数用来指定要删除的字符
print 'Hen,fuck is not a good word'.translate(table,' ')	#将空格都删除

# 字符串的方法有很多，以上这些是比较常用的，可以用到时再去查。
# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/04/2991050.html