
# coding=utf-8
"""
 Copyright (c) 2014, TP-Link Co,Ltd.
 Author: chenbiren <chenbiren@tp-link.net>
 Updated: 2014/10/14
"""
from tornado.httputil import HTTPHeaders
from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest
from tornado.web import HTTPError

default_headers = {
    'content-type': "application/json;encoding=UTF-8"
}

class Service(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(cls, Service).__new__(cls)
        return cls._instance

    def __init__(self):
        self.http = HTTPClient()

    def post(self, request, **kwargs):
        if not isinstance(request, HTTPRequest):
            kwargs['method'] = 'POST'
        else:
            request.method = 'POST'
        return self.fetch(request, **kwargs)


    def get(self, request, **kwargs):
        if not isinstance(request, HTTPRequest):
            kwargs['method'] = 'GET'
        else:
            request.method = 'GET'
        return self.fetch(request, **kwargs)

    def fetch(self, request, **kwargs):
        headers = kwargs['headers'] if 'headers' in kwargs else default_headers
        if not isinstance(request, HTTPRequest):
            request = HTTPRequest(url=request, headers = headers, **kwargs)
        request.headers = HTTPHeaders(request.headers if request.headers else headers)
        try:
            return self.http.fetch(request)
        except (HTTPError, SyntaxError), e:
            #todo log
            print "[ERROR]", e

class AsyncService(object):
    def __new__(cls, io_loop):
        if not hasattr(cls, "_instance"):
            cls._instance = super(cls, AsyncService).__new__(cls, io_loop)
        return cls._instance

    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.http = AsyncHTTPClient(io_loop)

    def post(self, request, callback, **kwargs):
        if not isinstance(request, HTTPRequest):
            kwargs['method'] = 'POST'
        else:
            request.method = 'POST'
        return self.fetch(request,callback, **kwargs)


    def get(self, request, callback, **kwargs):
        if not isinstance(request, HTTPRequest):
            kwargs['method'] = 'GET'
        else:
            request.method = 'GET'
        return self.fetch(request, callback, **kwargs)

    def fetch(self, request, callback, **kwargs):
        headers = kwargs['headers'] if 'headers' in kwargs else default_headers
        if not isinstance(request, HTTPRequest):
            request = HTTPRequest(url=request, headers = headers, **kwargs)
        request.headers = HTTPHeaders(request.headers if request.headers else headers)
        return self.http.fetch(request, callback)

if __name__ == "__main__":
    import tornado.ioloop
    ioloop = tornado.ioloop.IOLoop.instance()
    service = AsyncService(io_loop=ioloop)
    def handler(response):
        if response.error:
            print "Error"
        else:
            print response.body
    body = str({'method':'getDeviceList'})
    default_url = "http://172.29.88.120:12080?token=81d178b85b96492e91b8a71cfc907053"
    for i in range(100):
        service.post(default_url, handler, body=body)
    ioloop.start()
