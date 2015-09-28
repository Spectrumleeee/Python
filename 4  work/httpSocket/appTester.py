#coding=utf-8
import re
import sys,os,json
import urllib,urllib2
from time import *

class NetUtil():
	def getHtml(self, url, enable_proxy):
		enable_proxy = enable_proxy				# 配置是否使用代理
		proxy_handler = urllib2.ProxyHandler({'http' : 'http://127.0.0.1:8087'})
		null_proxy_handler = urllib2.ProxyHandler({})
	 
		if enable_proxy:
			opener = urllib2.build_opener(proxy_handler)
		else:
			opener = urllib2.build_opener(null_proxy_handler)
		urllib2.install_opener(opener)
		
		headers = {'content-type': 'application/json;charset=UTF-8'}		
		req = urllib2.Request(url, headers=headers)
		page = urllib2.urlopen(req)
		html = page.read()
		return html

class AppTester():
	def __init__(self):
		self.headers = {'content-type': 'application/json;charset=UTF-8'}
		self.url = 'http://172.29.88.120:12080'

	def send_post(self, url, params):
		data = json.dumps(params)
		print "[INFO]\tRequest :", data
		req = urllib2.Request(url, data, headers=self.headers)
		response = urllib2.urlopen(req)
		resp = json.loads(response.read())
		return resp
		
	def test_loginByPassword(self, params):
		resp = self.send_post(self.url, params)
		token = resp['result']['token']
		print "[INFO]\tResponse:", resp
		return token
	
	def test_uploadDeviceConfig(self, token, params):
		resp = self.send_post(self.url + '?token=' + token , params)
		print "[INFO]\tResponse:", resp
		
if __name__ == '__main__':
	appTester = AppTester()

#	params_loginByPassword = {'method':'login', 'params':{'cloudUserName':'wujinqiang2@tp-link.net', 'cloudPassword':'12345678'}}
	params_loginByPassword = {'method':'login', 'params':{'cloudUserName':'test@tplinkyun.com', 'cloudPassword':'pass123456'}}
	token = appTester.test_loginByPassword(params_loginByPassword)
	
	params_uploadDeviceConfig_update = {'method':'uploadDeviceConfig', 'params': { 'deviceId':'DDDDEEEE00000000000000000000000000000010','update':[{'id': '902B34A99621', 'config':{'key1':'value1', 'key2':'value2'}}, {'id': '3293F34K341L', 'config':{'name':'你好', 'type':'HONOR'}}] }}
	params_uploadDeviceConfig_delete = {'method':'uploadDeviceConfig', 'params': { 'deviceId':'DDDDEEEE00000000000000000000000000000010', 'delete':['3293F34K341L'] }}
	params_uploadDeviceConfig_basic = {'method':'uploadDeviceConfig', 'params': { 'deviceId':'DDDDEEEE00000000000000000000000000000010','basic':{'name':'uat_device', 'ip':'59.40.98.188'}}}
	params_uploadDeviceConfig_empty = {'method':'uploadDeviceConfig', 'params': { 'deviceId':'DDDDEEEE00000000000000000000000000000010'}}

	appTester.test_uploadDeviceConfig(token, params_uploadDeviceConfig_update)
'''	appTester.test_uploadDeviceConfig(token, params_uploadDeviceConfig_delete)
	appTester.test_uploadDeviceConfig(token, params_uploadDeviceConfig_basic)
	appTester.test_uploadDeviceConfig(token, params_uploadDeviceConfig_empty)
'''

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	