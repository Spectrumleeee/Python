import tornado.web

class Handler(tornado.web.RequestHandler):
	"""
	"""
	def write_error(self, status_code, **kwargs):
		if status_code == 404:
			self.render('404.html')
		elif status_code == 500:
			self.render('500.html')
	def get_current_user(self):
		return self.get_secure_cookie('user')
		
class PageNotFoundHandler(Handler):
	def get(self):
		raise tornado.web.HTTPError(404, 'Page not Found.')

tornado.web.ErrorHandler = PageNotFoundHandler