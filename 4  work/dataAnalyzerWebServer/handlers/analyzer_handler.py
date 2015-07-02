from handler import Handler
from ui.search import SearchForm
from dao.mongoDao import *

class AnalyzerHandler(Handler):
	def get(self):
#		content = {"deviceid":"F2E81EF6ED84CB8AEC6CCEC682A0F000C5D7350B", "starttime":"20150501000000", "finishtime":"25150501000000"}
#		items = []
#		self.render('analyzer.html', items=items, **content)
#		self.render('tracking.html')
		self.render('analyzer.html')