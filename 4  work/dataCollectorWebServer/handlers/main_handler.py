from tornado.web import authenticated, MissingArgumentError
from handler import Handler
from dao.mongoDao import *
import json

class MainHandler(Handler):
	@authenticated
	def get(self):
		mongo = mongoDao()
		#items = ["Item 1", "Item 2", "Item 3"]
		items = []
		for item in mongo.queryAll(300000):
			del item['_id']
			items.append(json.dumps(item))
		content = {"deviceid":"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "starttime":"20150506111111", "finishtime":"20150507111111"}
		self.render('index.html', items=items, **content)
		#person = dict(name="spectrumleeee",sex="male")
		#self.write(person)
		