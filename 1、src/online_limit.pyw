#coding=utf-8

'''
===���ҳ����ƽű���
=== ������һ������ÿ������ʱ���ܺ�Ϊ2��Сʱ����������Ϊ4Сʱ
=== �ļ�thefile.txt��ʽ���£�
		01/10/2014
		20
===Ĭ��ʹ��pythonnw.exe����򿪣����ýű����õ�windows�����ļ�����ʵ�ֿ�������������ʹ�ã����Կ����������ڹر�pythonnw ����ȡ���ҳ�����
===REF:http://www.cnblogs.com/levenyes/p/4003681.html
'''

import os 
import time   
import datetime   

#�����Ƿ�������������ʱ��
if datetime.date.today().weekday()<5:
    timeLimit = 14
else:
    timeLimit = 400

#��ȡ�ı��м�¼������
f = open('E:\\thefile.txt','r+')
f_date = f.readline()
f.close

#��ȡϵͳ���ڣ������ı����ڽ��бȶ�
#�������ȣ�������ļ������е��ճ�ʼ��
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

#��ѭ����䣬���ҽ�������ʱ����ڵ�������ʱ��ʱ����ѭ��
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

#�ػ���������ػ���       
cmd="cmd.exe /k shutdown -s -t 0";

#ִ�йػ�����
os.system(cmd)