# coding=utf-8
# ����ѧϰ��Python��ʹ�� ������ʽ��regular expression, ��� RE��

# Python RE --- ����Ԫ�ַ���meta character��& �﷨��syntax��														REF-1
'''
���﷨��		��˵����									�����ʽʵ����			������ƥ����ַ�����
һ���ַ�		ƥ������										abc							abc
.				ƥ�����⻻�з���\n������ַ�						a.c 						abc 
				��DOTALLģʽ��Ҳ��ƥ�任�з�
\				ת���ַ���ʹ��һ���ַ��ı�ԭ������˼			a\.c   						a.c 
				����ַ����������ַ���Ҫƥ�����				a\\c 						a\c
[...]			�ַ�������Ӧ��λ�ÿ������ַ����������ַ���		a[bcd]e 					abe 
				�ַ�����������г���Ҳ���Ը�����Χ����[abcd]��  a[bcd]e                     ace
				[a-d]����һ���ַ������^��ʾȡ������[^abc]��ʾ  a[bcd]e 					ade
				����abc������ĳ���ַ���

\d 				����:[0-9]										a\dc						a1c��a2c��a3c
\D 				������:[^\d]									a\Dc 						abc
\s 				�հ��ַ�:[<�ո�>\t\r\n\f\v]						a\sc 						a c
\S 				�ǿհ��ַ�:[^\s]  								a\Sc						abc
\w 				�����ַ�:[A-Za-z0-9_]							a\wc						abc
\W 				�ǵ����ַ�:[^\w]								a\Wc						a c

*				ƥ��ǰһ���ַ�0�����޴�							abc*						ab��abccc
+				ƥ��ǰһ���ַ�1�����޴�							abc+						abc��abccc
?				ƥ��ǰһ���ַ�0�λ�1��							abc?						ab��abc
{m}				ƥ��ǰһ���ַ�m��								ab{2}c  					abbc
{m,n}			ƥ��ǰһ���ַ�m��n��							ab{1,2}c 					abc��abbc

^				ƥ���ַ�����ͷ���ڶ���ģʽ��ƥ��ÿһ�еĿ�ͷ    ^abc 						abc
$				ƥ���ַ���ĩβ���ڶ���ģʽ��ƥ��ÿһ�е�ĩβ    abc$						abc
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

pattern = re.compile(r'(\w+) (.+l)') 					# ƥ�䵽���� l, Ĭ��̰��ģʽ
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

pattern = re.compile(r'(\w+) (.*)') 					# �ֳ������飬����Ԫ��֮���ǿո�
match = pattern.match('world hello world1 world2 !')
print match.groups()
a = match.groups()
print a[1],a[0]
print '*'*40

pattern = re.compile(r'(\w* \w* \w* \w*) (.)') 		     # �ֳ������飬����Ԫ��֮���ǿո�
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














