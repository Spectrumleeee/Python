#coding=utf-8
import sys
from handler import Handler
from service.stocks import *

class StocksHandler(Handler):
	stockStr = "sz000705,sz000599,sz002475,sz000729,sh600546"
	strockShSzStr = "s_sh000001,s_sz399001"
	
	def get(self):
		stocksData = Stocks()
		stocks = stocksData.get_stock0(self.stockStr)
		stocks_sh_sz = stocksData.get_stock0(self.strockShSzStr)
		self.render('stocks.html', stocks=stocks, stocks_sh_sz=stocks_sh_sz)
		
	def post(self):
#		print self.get_argument("username"), self.get_argument("password")
#		print self.request.host, self.request.uri
		stocksData = Stocks()
		stocks = stocksData.get_stock0(self.stockStr)
		stocks_sh_sz = stocksData.get_stock0(self.strockShSzStr)
		
		for stock in stocks:
			stock[0] = stock[0].decode(encoding="gbk")
		for stock in stocks_sh_sz:
			stock[0] = stock[0].decode(encoding="gbk")
	
		jsonData = {}
		jsonData["stocks"] = stocks
		jsonData["stocks_sh_sz"] = stocks_sh_sz
		self.write(jsonData)
#		jsonObj["stocks"] = ["\xb3\xa4".decode(encoding="gbk")] 
#		print jsonObj["stocks"][0].encode(encoding="gbk")