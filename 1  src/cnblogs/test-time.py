# coding=utf-8

# time --- time()
from time import *								# 导入python模块的所有函数 就可以直接调用内部函数
print time()

# time --- localtime()							# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print localtime()
print localtime()[:6]
print localtime(time())
print localtime(1370485361.442)
print localtime(345)							# 默认从1970年1月1日开始
print localtime(1)

# time --- gmtime()								# 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
print gmtime()
print gmtime(time())

# time --- asctime()							# 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'
print asctime()
print asctime(localtime())

# time --- ctime()								# 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
print ctime()
print ctime(time())
print ctime(238)
print ctime(1)

# time --- strftime(format[, tuple])			# 把一个代表时间的元组或者struct_time转化为格式化的时间字符串
print strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
print strftime('%Y-%m-%d %H:%M:%S', localtime())
print strftime('%Y-%m-%d %X', localtime())

# time --- mktime()								# 将一个struct_time或者9个参数的时间元组转化为时间戳
print mktime(localtime())
print mktime((2013, 6, 6, 13, 3, 38, 1, 48, 0))

# time ---strptime(string[, format])			# 把一个格式化时间字符串转化为struct_time。它是strftime()的逆操作。
print strptime('2013-06-06 11:12:39','%Y-%m-%d %X')

# time --- sleep(secs)							# 挂起当前的进程
sleep(1)

# time --- clock()								
'''在Linux系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。在windows操作系统上，time.clock()返回第一次调用该方法到现在的秒数，其精确度高于1微秒。可以使用该函数来记录程序执行的时间。'''
print clock()									# 在第一次调用的时候，返回的是程序运行的实际时间
print clock()									# 以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔

# time --- summary
'''
   time.time() 														获取当前时间戳
   time.localtime() 												当前时间的struct_time形式
   time.ctime() 													当前时间的字符串形式
   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())				将时间戳转换为字符串
   time.mktime(time.strptime('2013-06-06 09:00','%Y-%m-%d %H:%M'))	将字符串转换为时间戳
   
   Python中时间的三种表示方式
		1）、timestamp
		2）、tuple或者struct_time
		3）、格式化字符串。
'''

# REF: http://www.cnblogs.com/zhoujie/archive/2013/06/06/3120766.html