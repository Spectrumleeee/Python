# coding=utf-8
# 测试学习在Python中使用 正则表达式（regular expression, 简称 RE）

# Python RE --- 正则元字符（meta character）& 语法（syntax）														REF-1
'''
【语法】		【说明】									【表达式实例】			【完整匹配的字符串】
一般字符		匹配自身										abc							abc
.				匹配任意换行符“\n”外的字符						a.c 						abc 
				在DOTALL模式中也能匹配换行符
\				转义字符，使后一个字符改变原来的意思			a\.c   						a.c 
				如果字符串有特殊字符需要匹配可用				a\\c 						a\c
[...]			字符集。对应的位置可以是字符集中任意字符。		a[bcd]e 					abe 
				字符集可以逐个列出，也可以给出范围，如[abcd]或  a[bcd]e                     ace
				[a-d]。第一个字符如果是^表示取反，如[^abc]表示  a[bcd]e 					ade
				不是abc的其它某个字符。

\d 				数字:[0-9]										a\dc						a1c、a2c、a3c
\D 				非数字:[^\d]									a\Dc 						abc
\s 				空白字符:[<空格>\t\r\n\f\v]						a\sc 						a c
\S 				非空白字符:[^\s]  								a\Sc						abc
\w 				单词字符:[A-Za-z0-9_]							a\wc						abc
\W 				非单词字符:[^\w]								a\Wc						a c

*				匹配前一个字符0或无限次							abc*						ab、abccc
+				匹配前一个字符1或无限次							abc+						abc、abccc
?				匹配前一个字符0次或1次							abc?						ab、abc
{m}				匹配前一个字符m次								ab{2}c  					abbc
{m,n}			匹配前一个字符m至n次							ab{1,2}c 					abc、abbc

^				匹配字符串开头，在多行模式中匹配每一行的开头    ^abc 						abc
$				匹配字符串末尾，在多行模式中匹配每一行的末尾    abc$						abc
'''

import re
# Python RE --- compile & search
pattern = re.compile(r'world') 
match = pattern.search('hello world1 world2 !') 
print match.group()
print '*'*40

# Python RE --- compile & match
pattern = re.compile(r'(\w+) (\w+)') 
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

pattern = re.compile(r'(\w+) (.+l)') 					# 匹配到最后的 l, 默认贪婪模式
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

pattern = re.compile(r'(\w+) (.+2)') 
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

pattern = re.compile(r'(\w+) (.*)') 					# 分成两个组，两个元组之间是空格
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

pattern = re.compile(r'(\w* \w* \w* \w*) (.)') 		     # 分成两个组，两个元组之间是空格
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

# Python RE --- compile & split 
p = re.compile(r'\d+')
print p.split('one1two2three3four4')
print '*'*40

# Python RE --- compile & findall
p = re.compile(r'\d+')
print p.findall('one11two22three33four44')
print '*'*40

# Python RE --- compile & finditer
p = re.compile(r'\d+')
for m in p.finditer('one11two22three33four44'):
	print m.group(),
print
print '*'*40

# Python RE --- compile & sub
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print p.sub(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.sub(func, s)
print '*'*40

# Python RE --- compile & subn
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print p.subn(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.subn(func, s)













# REF-1:  http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html














