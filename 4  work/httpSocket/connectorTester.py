#coding=utf-8

import socket, ssl, pprint, certifi
from time import *
from struct import *

class Client():
	
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.CommonMagic = bytearray([0xA1,0xB2])
		self.CollectorMagic = bytearray([0xA1,0xB3])
#		print self.magic, self.length

	def connect(self, ip = None, port = None):
		if ip == None:
			ip = self.ip
		if port == None:
			port = self.port
	
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		certifiPath = certifi.where()
		self.ssl_socket = ssl.wrap_socket(sock, ca_certs=certifiPath, cert_reqs=ssl.CERT_REQUIRED)
		self.ssl_socket.connect((ip, port))	
		print "[OK]\tconnect to the connector!"
	
	def sendMessage(self, message):
		length = pack('!h',len(message))
		self.ssl_socket.write(self.CommonMagic)
		self.ssl_socket.write(length)
		self.ssl_socket.write(message)
		print "[OK]\tsend a message!"
		receivedMagic = self.ssl_socket.read(2)
		if receivedMagic == self.CommonMagic:
			print "Common Message"
		elif receivedMagic == self.CollectorMagic:
			print "Collector Message"
		
		
		
#	def sendCollectorMessage(self, message):
		
		
	
	
if __name__ == '__main__':
	client = Client('172.29.88.120', 50443)
	client.connect()
	heartBeat = bytes(r'{"id":111,"method":"heartBeat"}')
	client.sendMessage(heartBeat)
#	client.sendMessage(heartBeat)
#	client.sendMessage(heartBeat)
	
	

