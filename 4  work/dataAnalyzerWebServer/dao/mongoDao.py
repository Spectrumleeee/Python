import pymongo
import json
from tornado.options import define, options
from time import *
define('mongodbip', default = '172.29.88.113', help = 'mongodb ip addres', type = str)
define('mongodbport', default = 27017, help = 'mongodb ip addres', type = int)
define('mongodbdatabase', default = 'formal', help = 'mongodb database', type = str)
define('mongodbcollection', default = 'collector', help = 'mongodb collection', type = str)

class mongoDao():
	def __init__(self, database = None, collection = None):
		conn = pymongo.MongoClient(options.mongodbip, options.mongodbport)
		if database == None:
			database = options.mongodbdatabase
		if collection == None:
			collection = options.mongodbcollection
		db = conn[database]
		self.coll = db[collection]

	def queryAll(self):
		return self.coll.find()

	def query0(self, deviceid, starttime, finishtime):
		jsonArray = [{"receivedTime": {"$gt": starttime}}, {"receivedTime": {"$lt": finishtime}}]
		if len(deviceid) == 40:
			jsonArray.append({"deviceId":deviceid})
		jsonObj = {"$and" : jsonArray }
		print jsonObj
		return self.coll.find(jsonObj)
	
	def query(self, jsonObj):
		return self.coll.find(jsonObj)
		
	def persist(self):
		currTime = strftime('%Y%m%d%H%M%S', localtime(time()));
		user = {"name":"cui","age":"10", "receivedTime":currTime}
		self.coll.insert(user)
	
	def persist(self, jsonObj):
		self.coll.insert(jsonObj)

def main():
	mongo = mongoDao()

if __name__ == '__main__':
	main()

