#coding=utf-8
import MySQLdb

class MysqlDAO():
	def __init__(self, host = '127.0.0.1', passwd='cloud', db = 'cloud', port = 3306, user='cloud'):
		self.conn = MySQLdb.connect(host, user, passwd, db, port)
		self.cur=self.conn.cursor()
	
	def queryAll(self, table):
		try:
			count=self.cur.execute('select * from %s' % table)
			results=self.cur.fetchall()
			for rst in results:
				print rst
		except MySQLdb.Error, e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])		

	def updateById(self, table, setKey, setValue, idName, idValue):
		try:
			self.cur.execute('update %s set %s=%s where %s=%s' %(table, setKey, setValue, idName, idValue))
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	def deleteById(self, table, idName, idValue):
		try:
			self.cur.execute("delete from %s where %s=%s" %(table, idName, idValue))
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	
		
	def insert(self, table, fields=[], values=[]):
		try:
			sql='insert into %s(%s) values(%s)' %(table, ",".join(fields), ",".join(values))
			print sql
			self.cur.execute(sql)
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	def close(self):
		self.cur.close()
		self.conn.close()

def main():
	mysql=MysqlDAO()
#	mysql.queryAll('account')
#	mysql.insert("app_info", ["account_id", "app_type", "version_code"], ["2000", r"'IOS'", "10384"])
#	mysql.insert("app_info", ["account_id", "app_type", "version_code"], ["2001", r"'ANDROID'", "10384"])
#	mysql.insert("app_info", ["account_id", "app_type", "version_code"], ["2002", r"'IOS'", "10384"])
#	mysql.insert("app_info", ["account_id", "token"], ["2003", r"'token_test'"])

	mysql.deleteById('app_info', 'account_id', '2000')
#	mysql.queryAll('device')
#	mysql.updateById('app_info', 'version_code', "9527", 'account_id', "1003")
#	mysql.updateById('app_info', 'version_code', "10", 'account_id', "1001")
	
	mysql.close()

if __name__ == '__main__':
	main()
