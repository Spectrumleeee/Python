from handler import Handler
from ui.user import LoginForm

def test():
	default_url = "http://abc.com"
	params = {'url':'http://baidu.com'}
	url = getattr(params, 'url', default_url)
	print url
	
class LoginHandler(Handler):
	def get(self):
		self.render('account.html')
		
	def post(self):
		form = LoginForm(self)

		if not form.validate():
			print(form.errors)
			return
		username = form.email.data.encode(encoding='utf-8')
		password = form.password.data.encode(encoding='utf-8')
		print username, password
		test()
