#coding=utf-8
import urllib,json,socket  
import random,os  
import sys,datetime  
  
starttime = datetime.datetime.now()  
socket.setdefaulttimeout(10)   
dir ='D:\\Documents and Settings\\Documents\\GitHub\Python\\3  pics\\picture_crawler\\abc\\'  
if not os.path.isdir(dir):  
    os.mkdir(dir)  
i=0  
j=1  
p=30
while i<10:
	if i%2==0:
#       http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%90%9E%E7%AC%91&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn=30&rn=60&requestType=1&1357639151100
#		url ='http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%91%84%E5%BD%B1&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn='+str(p*i)+'&rn=60&requestType=1&'+str(random.random())
#		url ='http://image.baidu.com/channel/listjson?fr=channel&tag1=%E7%BE%8E%E5%A5%B3&tag2=%E5%B0%8F%E6%B8%85%E6%96%B0&sorttype=0&pn='+str(p*i)+'&rn=60&ie=utf8&oe=utf-8&'+str(random.random())
#		url ='http://image.baidu.com/channel/listjson?fr=channel&tag1=%e5%86%9b%e4%ba%8b&tag2=%E7%A9%BA%E5%86%9B&sorttype=0&pn='+str(p*i)+'&rn=60&ie=utf8&oe=utf-8&'+str(random.random())				# REF-1
#		url ='http://image.baidu.com/data/data?col=%E5%86%9B%E4%BA%8B&tag=%E7%A9%BA%E5%86%9B&sort=0&tag3=&pn=120&rn=60&p=channel&from=1'
#		url ='http://image.baidu.com/channel/listjson?fr=channel&tag1=军事&tag2=海军&sorttype=0&pn='+str(p*i)+'&rn=60&ie=utf8&oe=utf-8&'+str(random.random())				
#		url ='http://image.baidu.com/channel/listjson?fr=channel&tag1=设计&tag2=灵感&sorttype=0&pn='+str(p*i)+'&rn=60&ie=utf8&oe=utf-8&'+str(random.random())
#		url ='http://image.baidu.com/i?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1414574910750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=鲨鱼'
		print url
		try:
			ipdata = urllib.urlopen(url).read()
#			print ipdata
		except IOError,e:
			#if e.message=="time out":
			print('img %s_%s is false1' % (i,j) )
			break
	else:
		ipdata1 = json.loads(ipdata)
		if ipdata1['data']:
			for n in ipdata1['data']:
				if n and n['image_url']:
					try:
						print n['image_url']
						dataimg = urllib.urlopen(n['image_url']).read()
					except IOError,e:
						#if e.message=="time out":
						print('img %s_%s is false2' % (i,j))
						break
					else:
						fPostfix = os.path.splitext(n['image_url'])[1]
						if (fPostfix == '.png' or fPostfix == '.jpg' or fPostfix == '.PNG' or fPostfix == '.JPG'):
							filename = dir+os.path.basename(n['image_url'])
						else:
							filename = dir+os.path.basename(n['image_url'])+'.jpg'
						try:
							urllib.urlretrieve(n['image_url'],'%s' %filename)
#							file_object = open(filename,'w')
#							file_object.write(dataimg)
#							file_object.close()
						except socket.timeout,e:
							#if e.message=="timed out":
							print('img %s_%s is false3' % (i,j) )
							break
						else:
							#urllib.urlretrieve(n['image_url'],filename)
							print('img %s_%s is ok' % (i,j) )
							j +=1
				else:
					break
	i +=1
endtime = datetime.datetime.now()  
print 'spend %s seconds' % (endtime-starttime).seconds  
sys.exit() 

#REF-1: http://www.convertstring.com/zh_CN/EncodeDecode/UrlEncode
#REF-2: http://blog.csdn.net/lerdor/article/details/12047447