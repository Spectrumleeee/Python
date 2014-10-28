# coding=utf-8

# mysql --- query 
'''
import MySQLdb as mdb
db = mdb.connect(server_ip, username, password, db_name)
cur = db.cursor()
cur.execute('select * from account;')
for data in cur.fetchall():
	print data[1]
db.close

# mysql --- create database
import MySQLdb as mdb
file = open("D:\\Documents and Settings\\Desktop\\config.txt")
config = file.readline()
param = list(config.split(' '))
db = mdb.connect(*param)
cur = db.cursor()
try:
	cur.execute('create database db_name')
	db.commit()
except:
	db.rollback()
db.close
'''

# mysql --- create table and insert
import MySQLdb as mdb					# REF-B					
import datetime
import time
import os

def insert():
	for i in range(1,50):
		sqlstr = "insert into hello values(%s,'spectrumleeee', '%s')" %(i, datetime.datetime(*time.localtime()[:6]))	# REF-E
#		print sqlstr
		cur.execute(sqlstr)

file = open("D:\\Documents and Settings\\Desktop\\config.txt")
config = file.readline()
param = list(config.split(' '))
#print param
db = mdb.connect(*param)
cur = db.cursor()
try:
	cur.execute('create table if not exists hello(number INT(1) primary key, name VARCHAR(255), birthday DATETIME)')
	insert()
	db.commit()
except mdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	db.rollback()
cur.close
db.close
file.close


# REF-A: http://www.cnblogs.com/zhoujie/archive/2013/06/07/3125367.html
# REF-B: http://wangjunle23.blog.163.com/blog/static/117838171201331461444367/
# REF-C: http://blog.csdn.net/yelbosh/article/details/7498641
# REF-D: http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html
# REF-E: http://www.educity.cn/wenda/353573.html

