#coding=utf-8
import re
import sys,os
import urllib,urllib2
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from dao.mongoDao import *
from time import *

class NetUtil():
	def getHtml(self, url, enable_proxy):
		enable_proxy = enable_proxy				# 配置是否使用代理
		proxy_handler = urllib2.ProxyHandler({"http" : 'http://127.0.0.1:8087'})
		null_proxy_handler = urllib2.ProxyHandler({})
	 
		if enable_proxy:
			opener = urllib2.build_opener(proxy_handler)
		else:
			opener = urllib2.build_opener(null_proxy_handler)
		urllib2.install_opener(opener)
		
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0'}		#伪造成浏览器访问，很多网站禁止直接爬虫访问
		req = urllib2.Request(url, headers=headers)
		page = urllib2.urlopen(req)
		html = page.read()
		return html

class Stocks():
	def __init__(self):
		self.urlPrefix = "http://hq.sinajs.cn/list="
		self.netUtil = NetUtil()
		regStr = r'"[\s\S]*"'
		self.stockRe = re.compile(regStr)
		
	def get_stock0(self, stock_code):
		stock_url = self.urlPrefix + stock_code
		resp = self.netUtil.getHtml(stock_url, False)
		resp = resp.split('\n')
		stocks = []
		for eachStock in resp:
			stock_specific = self.stockRe.findall(eachStock)
			if len(stock_specific) == 1:
				stocks.append(stock_specific[0].replace(r'"','').split(","))
		return stocks
	
	def get_stock_sh(self):
		return self.get_stock0('s_sh000001')
		
	def get_stock_sz(self):
		return self.get_stock0('s_sz399001')
		
	def get_stock(self, stock_code):
		if stock_code[0] == '6':
			stock_code = 'sh' + stock_code
		elif stock_code[0] == '0':
			stock_code = 'sz' + stock_code
		else:
			print "error code"
			return
		return self.get_stock0(stock_code)

# 查询数据库，显示历史数据
def showStocksHistory():
	mongo = mongoDao("test", "stocks")

	for stockItem in mongo.queryAll():
		del stockItem['_id']
		
		print "sh ", stockItem["sh"],
		for stock in stockItem["stocks"]:
			for it, value in stock.items():
				print it.encode(encoding="gbk"), value,
		print stockItem["time"]	

# 每隔interval秒显示指定个股信息到控制台，每隔round个周期持久化一次当前股票信息（interval*round秒）
def showStocksCurrent(interval, round):
	stocksUtils = Stocks()
	mongo = mongoDao("test", "stocks")
	count = 0
	
	while 1 == 1:
#		stocks = stocksUtils.get_stock0('s_sh000001,sz000507,sh601933,sz002056,sh600485')
		stocks = stocksUtils.get_stock0('s_sh000001,sh601933,sz002142,sz000571')
		allStocks = []
		for stock in stocks:
			if len(stock) == 6:
#				print stock[0], stock[1],
				print "SH", stock[1],
				sh = stock[1]
				continue
			print stock[0], stock[3], stock[4], stock[5],
#			print "STOCKS", stock[3], stock[4], stock[5],
			allStocks.append({stock[0].decode(encoding="gbk"): stock[3]})
		print
		
		if count == round :
			currTime = strftime('%Y%m%d%H%M%S', localtime(time()));
			mongo.persist({"time":currTime, "stocks":allStocks, "sh": sh})
			count = 0
		
		sleep(interval)
		count += 1
	
if __name__ == '__main__':
	showStocksCurrent(30,10)
#	showStocksHistory()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	