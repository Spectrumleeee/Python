import pymongo
import json
from tornado.options import define, options
from time import *
define('mongodbip', default = '172.29.88.113', help = 'mongodb ip addres', type = str)
define('mongodbport', default = 27017, help = 'mongodb ip addres', type = int)

class mongoDao():
	def __init__(self):
		conn = pymongo.MongoClient(options.mongodbip, options.mongodbport)
		print options.mongodbip
		db = conn.formal
		self.coll = db.collector

	def queryAll(self, interval):
		currTime = strftime('%Y%m%d%H%M%S', localtime(time() - interval))
		return self.coll.find({'receivedTime':{'$gt':currTime}})

	def query(self, deviceid, starttime, finishtime):
		jsonArray = [{"receivedTime": {"$gt": starttime}}, {"receivedTime": {"$lt": finishtime}}]
		if len(deviceid) == 40:
			jsonArray.append({"deviceId":deviceid})
		jsonObj = {"$and" : jsonArray }
		print jsonObj
		return self.coll.find(jsonObj)

	def persist(self):
		currTime = strftime('%Y%m%d%H%M%S', localtime(time()));
		user = {"name":"cui","age":"10", "receivedTime":currTime}
		self.coll.insert(user)

def main():
	mongo = mongoDao()
	data = []
	for item in mongo.queryAll(3000000):
		del item['_id']
		data.append(item)
	print data
	#mongo.persist()

if __name__ == '__main__':
	main()

