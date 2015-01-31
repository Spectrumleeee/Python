from tornado.web import authenticated, MissingArgumentError
from handler import Handler

class MainHandler(Handler):
	@authenticated
	def get(self):
		self.render('index.html')
		#person = dict(name="spectrumleeee",sex="male")
		#self.write(person)
		