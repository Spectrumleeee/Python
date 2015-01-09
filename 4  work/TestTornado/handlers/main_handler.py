from tornado.web import authenticated, MissingArgumentError
from handler import Handler

class MainHandler(Handler):
	@authenticated
	def get(self):
		self.render('index.html')
		