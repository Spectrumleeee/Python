#coding=utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from handlers.user_handler import *
from handlers.main_handler import *
from handlers.about_handler import *
define('port', default = 8888, help = 'run on the given port', type = int)
define('host', default = 'localhost', help = 'run on the given host', type = str)

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			xsrf_cookies = True,
			cookie_secret = "cookie_secret_code",
			autoreload = False,
			login_url = "/login",
			autoescape = None,
		)
		
		handlers = [
			(r"/", MainHandler),
			(r"/login", LoginHandler),
			(r"/about", AboutHandler)
		]
		
		tornado.web.Application.__init__(self, handlers, **settings)

def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	print("Server start at port:[%d]" % options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt, interrupt:
		import sys
		print('Server stop')
		tornado.ioloop.IOLoop.instance().stop()
		sys.exit(0)
