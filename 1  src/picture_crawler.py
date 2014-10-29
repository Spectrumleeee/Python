# coding=utf-8

import re
import sys,os
import urllib,urllib2

def getHtml(url, enable_proxy):
#    page = urllib.urlopen(url)
#    html = page.read()

	enable_proxy = enable_proxy				# �����Ƿ�ʹ�ô���
	proxy_handler = urllib2.ProxyHandler({"http" : 'http://127.0.0.1:8087'})
	null_proxy_handler = urllib2.ProxyHandler({})
 
	if enable_proxy:
		opener = urllib2.build_opener(proxy_handler)
	else:
		opener = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(opener)
	
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0'}		#α�����������ʣ��ܶ���վ��ֱֹ���������
	req = urllib2.Request(url, headers=headers)
	page = urllib2.urlopen(req)
	html = page.read()
	return html

def getImg(save_path,html,reg):
	if not os.path.exists(save_path):
		os.mkdir(save_path)
	print 'download begin...'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	for imgurl in imglist:
		print imgurl
		urllib.urlretrieve(imgurl,'%s%s.jpg' %(save_path,x))
		x = x + 1        
	print 'download finished...'

def download(url, enable_proxy, save_path, reg):
	html = getHtml(url, enable_proxy)
	type = sys.getfilesystemencoding()
	html.decode("gb2312").encode(type)
	getImg(save_path, html, reg)
'''
#html = getHtml("http://tieba.baidu.com/p/2460150866",True)
#html = getHtml("http://www.tp-link.com.cn/",False)
html = getHtml("http://www.oschina.net/",False)
type = sys.getfilesystemencoding()			# ��ȡ����ϵͳ���뷽ʽ					
html.decode("UTF-8").encode(type)		    # ���õ���ҳ��Դ���ñ��ر���ת�� ����������������	
save_path = 'D:\\Documents and Settings\\Documents\\GitHub\Python\\3  pics\\picture_crawler\\'
reg = r'http:\/\/[\w\.\/]+\.jpg'
getImg(save_path,html,reg)
'''
root_path = 'D:\\Documents and Settings\\Documents\\GitHub\Python\\3  pics\\picture_crawler\\'
reg = r'http:\/\/[\w\.\/=%]+\.jpg'
'''
url = 'http://www.oschina.net/'
my_path = 'oschinaa'
save_path = '%s%s\\' %(root_path,my_path)
download(url, False, save_path, reg)		# ��ʹ�ô���ֱ�����ؿ�Դ�й���ҳͼƬ

url = 'http://tieba.baidu.com/p/2460150866'	
my_path = 'tieba'
save_path = '%s%s\\' %(root_path,my_path)
download(url, True, save_path, reg)			# ʹ��goAgent��������������ͼƬ

word = '��ʿ����'
url = 'http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1414574910750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%s' % word
my_path = 'baidu_image'
save_path = '%s%s\\' %(root_path,my_path)
download(url, False, save_path, reg)
'''
url = 'http://www.taobao.com/'
my_path = 'www_taobao_com'
save_path = '%s%s\\' %(root_path,my_path)
download(url, False, save_path, reg)
