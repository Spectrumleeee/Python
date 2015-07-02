#coding=utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
import sys
from tornado.options import define, options
from handlers.user_handler import *
from handlers.main_handler import *
from handlers.about_handler import *
from handlers.search_handler import *
from handlers.analyzer_handler import *
from handlers.stocks_handler import *
define('port', default = 8888, help = 'run on the given port', type = int)
define('host', default = 'localhost', help = 'run on the given host', type = str)

class Application(tornado.web.Application):
	def __init__(self):
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			xsrf_cookies = False,
			cookie_secret = "cookie_secret_code",
			autoreload = True,
			login_url = "/login",
			autoescape = None,
			debug = True
		)
		
		handlers = [
#			(r"/", MainHandler),
#			(r"/login", LoginHandler),
#			(r"/about", AboutHandler),
			(r"/search", SearchHandler),
			(r"/analyzer", AnalyzerHandler),
			(r"/stocks", StocksHandler),
			(r"/", SearchHandler)
		]
		
		tornado.web.Application.__init__(self, handlers, **settings)

def main():
	reload(sys) 
	sys.setdefaultencoding("utf-8")
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	print("Server start at port:[%d]" % options.port)
	loop = tornado.ioloop.IOLoop.instance();
	loop.start()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt, interrupt:
		import sys
		print('Server stop')
		tornado.ioloop.IOLoop.instance().stop()
		sys.exit(0)
