# coding=utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from handlers.user_handler import *
from handlers.device_handler import *
define('port', default = 8888, help = 'run on the given port', type = int)
define('host', default = 'localhost', help = 'run on the given host', type = str)

tornado.options.parse_command_line()
print options.port, options.host