from handler import Handler
from ui.user import LoginForm
from service.account import loginByPassword

class LoginHandler(Handler):
	def get(self):
		self.render('login.html')
		
	def post(self):
		form = LoginForm(self)

		if not form.validate():
			print(form.errors)
			return
		username = form.email.data.encode(encoding='utf-8')
		password = form.password.data.encode(encoding='utf-8')
		print username, password
		bool = loginByPassword(username, password)
		if bool :
			self.set_secure_cookie('token', 'spectrumleeee')
			self.set_secure_cookie('user', username)
			self.redirect('/')
		else:
			self.render('404.html')
		
def test():
	default_url = "http://abc.com"
	params = {'url':'http://baidu.com'}
	url = getattr(params, 'url', default_url)
	print url