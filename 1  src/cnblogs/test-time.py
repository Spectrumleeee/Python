# coding=utf-8

# time --- time()
from time import *								# ����pythonģ������к��� �Ϳ���ֱ�ӵ����ڲ�����
print time()

# time --- localtime()							# ��һ��ʱ���ת��Ϊ��ǰʱ����struct_time��secs����δ�ṩ�����Ե�ǰʱ��Ϊ׼��
print localtime()
print localtime()[:6]
print localtime(time())
print localtime(1370485361.442)
print localtime(345)							# Ĭ�ϴ�1970��1��1�տ�ʼ
print localtime(1)

# time --- gmtime()								# ��localtime()�������ƣ�gmtime()�����ǽ�һ��ʱ���ת��ΪUTCʱ����0ʱ������struct_time��
print gmtime()
print gmtime(time())

# time --- asctime()							# ��һ����ʾʱ���Ԫ�����struct_time��ʾΪ������ʽ��'Sun Jun 20 23:21:05 1993'
print asctime()
print asctime(localtime())

# time --- ctime()								# ��һ��ʱ������������ĸ�������ת��Ϊtime.asctime()����ʽ
print ctime()
print ctime(time())
print ctime(238)
print ctime(1)

# time --- strftime(format[, tuple])			# ��һ������ʱ���Ԫ�����struct_timeת��Ϊ��ʽ����ʱ���ַ���
print strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
print strftime('%Y-%m-%d %H:%M:%S', localtime())
print strftime('%Y-%m-%d %X', localtime())

# time --- mktime()								# ��һ��struct_time����9��������ʱ��Ԫ��ת��Ϊʱ���
print mktime(localtime())
print mktime((2013, 6, 6, 13, 3, 38, 1, 48, 0))

# time ---strptime(string[, format])			# ��һ����ʽ��ʱ���ַ���ת��Ϊstruct_time������strftime()���������
print strptime('2013-06-06 11:12:39','%Y-%m-%d %X')

# time --- sleep(secs)							# ����ǰ�Ľ���
sleep(1)

# time --- clock()								
'''��Linuxϵͳ�ϣ������ص��ǡ�����ʱ�䡱�����������ʾ�ĸ�������ʱ���������windows����ϵͳ�ϣ�time.clock()���ص�һ�ε��ø÷��������ڵ��������侫ȷ�ȸ���1΢�롣����ʹ�øú�������¼����ִ�е�ʱ�䡣'''
print clock()									# �ڵ�һ�ε��õ�ʱ�򣬷��ص��ǳ������е�ʵ��ʱ��
print clock()									# �Եڶ���֮��ĵ��ã����ص����Ե�һ�ε��ú�,����ε��õ�ʱ����

# time --- summary
'''
   time.time() 														��ȡ��ǰʱ���
   time.localtime() 												��ǰʱ���struct_time��ʽ
   time.ctime() 													��ǰʱ����ַ�����ʽ
   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())				��ʱ���ת��Ϊ�ַ���
   time.mktime(time.strptime('2013-06-06 09:00','%Y-%m-%d %H:%M'))	���ַ���ת��Ϊʱ���
   
   Python��ʱ������ֱ�ʾ��ʽ
		1����timestamp
		2����tuple����struct_time
		3������ʽ���ַ�����
'''

# REF: http://www.cnblogs.com/zhoujie/archive/2013/06/06/3120766.html