#coding=utf-8

from pymouse import PyMouse											# REF-1
from time import *
from math import *
from ctypes import *

import win32api, win32con											# REF-2

User32dll = windll.User32
gdi32dll = windll.gdi32
hdc = User32dll.GetDC(None)
#print User32dll, gdi32dll

def getPix(x, y):													
	color = gdi32dll.GetPixel(hdc, x, y)   							# 获取屏幕鼠标位置像素值
	return color

m = PyMouse()
sleep(2)															# 程序睡眠两秒钟
print m.position()

while 1 < 2 and 2<3:
	sleep(1)
	m.press(2118,1065)												# 鼠标左键单击（x,y）
	sleep(1)
	m.press(2048,13)
	sleep(1)
	m.press(2910,198)
	sleep(20)
	m.press(3756,7)
	print 'waiting 5 mins ...'
	sleep(300)

'''
sleep(2)
color = getPix(*m.position())					
pixel = hex(color) 
print pixel
print m.position()
while(1 < 2):
	sleep(2)
	if getPix(*m.position()) != color:								# 判断两秒前后鼠标位置像素是否变化
		color = getPix(*m.position())
		print 'pixel changed !'	
	else:
		print 'pixel unchanged !'

'''
'''
i = 0
while 1 < 2:
	m.move(10+5*i,10+10*i)											# 移动鼠标到指定位置
	sleep(0.05)
	i+=1
	if i==100:
		i=0
'''

# REF-1: http://blog.sina.com.cn/s/blog_60b45f230101kucn.html
# REF-2: http://blog.csdn.net/daemonpei/article/details/8549246