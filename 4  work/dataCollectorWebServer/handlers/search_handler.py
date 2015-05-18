from handler import Handler
from ui.search import SearchForm
from dao.mongoDao import *

class SearchHandler(Handler):
	def get(self):
		content = {"deviceid":"F2E81EF6ED84CB8AEC6CCEC682A0F000C5D7350B", "starttime":"20150501000000", "finishtime":"25150501000000"}
		items = []
		self.render('index.html', items=items, **content)
		
	def post(self):
		form = SearchForm(self)

		if not form.validate():
			print(form.errors)
			return
		deviceid = form.deviceid.data.encode(encoding='utf-8')
		starttime = form.starttime.data.encode(encoding='utf-8')
		finishtime = form.finishtime.data.encode(encoding='utf-8')
		print deviceid, starttime, finishtime

		mongo = mongoDao()
		items = []
		for item in mongo.query(deviceid, starttime, finishtime):
			del item['_id']
			items.append(json.dumps(item))

		content = {"deviceid":deviceid, "starttime":starttime, "finishtime":finishtime}
		self.render('index.html', items=items, **content)