# coding=utf-8

import sqlite3						# 导入Python SQLITE数据库模块  Python2.5之后，内置了SQLite3，成为了内置模块

cx =  sqlite3.connect("D:\\Documents and Settings\\Documents\\GitHub\\Python\\1  src\\cnblogs\\test.db")	# 打开数据库连接
#con = sqlite3.connect(":memory:")    				# 创建数据库在内存中
cur = cx.cursor()
'''
sql_create_table = "create table if not exists catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)"
cur.execute(sql_create_table)						# 创建表
for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:		# 插入数据
    cur.execute("insert into catalog values (?,?,?,?)", t)
cx.commit()											# 不能用cx.commit,一定要加括号
'''
cur.execute('select * from catalog')				# 查找数据
for data in cur.fetchall():							# 逐条输出
	print data
cx.close()											# 关闭数据库连接

# REF-A: http://www.cnblogs.com/yuxc/archive/2011/08/18/2143606.html