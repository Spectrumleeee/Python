from handler import Handler

class AboutHandler(Handler):
	def get(self):
		self.render('about.html')