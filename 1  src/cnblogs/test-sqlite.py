# coding=utf-8

import sqlite3						# ����Python SQLITE���ݿ�ģ��  Python2.5֮��������SQLite3����Ϊ������ģ��

cx =  sqlite3.connect("D:\\Documents and Settings\\Documents\\GitHub\\Python\\1  src\\cnblogs\\test.db")	# �����ݿ�����
#con = sqlite3.connect(":memory:")    				# �������ݿ����ڴ���
cur = cx.cursor()
'''
sql_create_table = "create table if not exists catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)"
cur.execute(sql_create_table)						# ������
for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:		# ��������
    cur.execute("insert into catalog values (?,?,?,?)", t)
cx.commit()											# ������cx.commit,һ��Ҫ������
'''
cur.execute('select * from catalog')				# ��������
for data in cur.fetchall():							# �������
	print data
cx.close()											# �ر����ݿ�����



# REF-A: http://www.cnblogs.com/yuxc/archive/2011/08/18/2143606.html