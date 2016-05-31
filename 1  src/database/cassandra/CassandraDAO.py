from cassandra.cluster import Cluster

class CassandraDAO():
	def __init__(self, host = '127.0.0.1', portt=9042, ver=3, keyspace='cloud'):
		cluster = Cluster(contact_points=[host], port=portt, protocol_version=ver)
		self.session = cluster.connect(keyspace)
	
	def queryAll(self, table):
		rows = self.session.execute('select * from %s' %table)
		count=1
		for row in rows:
			print count, row.device_id, row.device_model_id
			count=count+1

	def insertIntoDevice(self, nums):
		for i in range(nums):
			deviceId = "DeviceVaServiceGetVaBalance" + str(i);
			self.session.execute("insert into device(device_id, device_model_id) values (%s, %s)",(deviceId, 9527))

	def deleteFromDevice(self, nums):
		for i in range(nums):
			deviceId = "DeviceVaServiceGetVaBalance" + str(i);
			self.session.execute("delete from device where device_id=%s", (deviceId,))

def main():
	cassa = CassandraDAO(host='172.31.1.162')
	
	cassa.queryAll('device')

	#cassa.deleteFromDevice(10000)
	cassa.insertIntoDevice(100)	

	cassa.queryAll('device')

if __name__ == '__main__':
	main()
