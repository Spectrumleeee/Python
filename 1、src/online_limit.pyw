#coding=utf-8

'''
===《家长控制脚本》
=== 限制周一到周五每天上网时间总和为2个小时，周六周日为4小时
=== 文件thefile.txt格式如下：
		01/10/2014
		20
===默认使用pythonnw.exe程序打开，将该脚本放置到windows启动文件夹中实现开机自启动本人使用，可以开机六分钟内关闭pythonnw 进程取消家长控制
===REF:http://www.cnblogs.com/levenyes/p/4003681.html
'''

import os 
import time   
import datetime   

#根据是否工作日设置限制时间
if datetime.date.today().weekday()<5:
    timeLimit = 14
else:
    timeLimit = 400

#读取文本中记录的日期
f = open('E:\\thefile.txt','r+')
f_date = f.readline()
f.close

#读取系统日期，并与文本日期进行比对
#如果不相等，则清空文件，进行当日初始化
n_date = time.strftime("%d/%m/%Y")+"\n"
if f_date != n_date:
    print("sucessed")
    f = open('E:\\thefile.txt','r+')
    f.truncate()
    f.close
    f = open('E:\\thefile.txt','r+')
    f.write((n_date))
    run_time="0"
    f.write(run_time)
    f.close

#死循环语句，当且仅当运行时间大于等于限制时间时跳出循环
while 2 > 1 :
    f = open('E:\\thefile.txt','r+')
    f_date = f.readline()
    run_time = f.readline()
    run = int(run_time)
    time.sleep(10)
    if run<timeLimit:
        run = run + 1
        f.truncate()
        f.close
        f = open('E:\\thefile.txt','r+')
        f.write(f_date)
        run_time = str(run)
        f.write(run_time)
        f.close
    else:
        break

#关机命令（立即关机）       
cmd="cmd.exe /k shutdown -s -t 0";

#执行关机命令
os.system(cmd)