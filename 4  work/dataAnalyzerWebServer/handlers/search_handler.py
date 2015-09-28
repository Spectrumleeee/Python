from handler import Handler
from ui.search import SearchForm
from dao.mongoDao import *
from time import *

class SearchHandler(Handler):
	def get(self):
		content = {"deviceid":"F2E81EF6ED84CB8AEC6CCEC682A0F000C5D7350B", "starttime":"20150501000000", "finishtime":"25150501000000", "spenttime": 0.0}
		items = []
		self.render('search.html', items=items, **content)
		
	def post(self):
		form = SearchForm(self)

		if not form.validate():
			print(form.errors)
			return
		deviceid = form.deviceid.data.encode()
		starttime = form.starttime.data.encode()
		finishtime = form.finishtime.data.encode()
		print deviceid, starttime, finishtime

		mongo = mongoDao()
		items = []
		
		startedTime = time()
		print startedTime
		for item in mongo.query0(deviceid, starttime, finishtime):
			del item['_id']
			items.append(json.dumps(item))
		spentTime = time() - startedTime;
		
		content = {"deviceid":deviceid, "starttime":starttime, "finishtime":finishtime, "spenttime": spentTime}
		self.render('search.html', items=items, **content)