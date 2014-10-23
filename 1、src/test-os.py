# coding=utf-8

# os --- getcwd() 提取当前目录
import os
s = os.getcwd()
print 'your location', s		# windows cmd命令 python test-os.py 
'''
import time
folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
os.makedirs(r'%s/%s'%(os.getcwd(),folder))
'''

# os --- makedirs() & rmdir()
os.makedirs("c:\\temp\\test")
os.rmdir("c:\\temp\\test")		# 注意只删除了test目录
os.rmdir("c:\\temp")			# 这里才删除了temp目录
	
# os --- os.path.split()		将路径分解为目录名和文件名
a,b = os.path.split("c:\\dir1\\dir2\\file.txt")
print a
print b

# os --- os.path.splitext()		分解文件名的扩展名
a,b=os.path.splitext("c:\\dir1\\dir2\\file.txt")
print a
print b

# os --- os.path.exists()
print os.path.exists("C:\\")
print os.path.exists("C:\\123\\")
print os.path.exists("C:\\123.txt")
print os.path.exists("C:\\关机.bat")

# os --- os.path.isfile()
print os.path.isfile("C:\\关机.bat")
print os.path.isfile("C:\\Python27")

# os --- os.path.isdir()
print os.path.isdir("C:\\关机.bat")
print os.path.isdir("C:\\Python27")

# os --- os.listdir()
#print os.listdir("C:\\")

def getDirList( p ):			# 获取指定目录下的所有子目录的列表
	p = str( p )
	if p=="":
		  return [ ]
	p = p.replace( "/","\\")
	if p[ -1] != "\\":
		 p = p+"\\"
	a = os.listdir( p )
	b = [ x   for x in a if os.path.isdir( p + x ) ]
	return b
#print getDirList( "C:\\" )

def getFileList( p ):			# 获取指定目录下所有文件的列表
	p = str( p )
	if p=="":
		  return [ ]
	p = p.replace( "/","\\")
	if p[ -1] != "\\":
		 p = p+"\\"
	a = os.listdir( p )
	b = [ x   for x in a if os.path.isfile( p + x ) ]
	return b
#print getFileList( "C:\\" )

# os --- open('file'[,'mode']) & read() & write() & seek() & tell()  
file = open("C:\\当前时间.bat")
print file.read()
file.seek(0)
print file.read(9)
print file.tell()
print file.read()
file.seek(0)
print file.tell()
file.seek(0)
print file.readline()
print file.tell()
print file.name
file.close()

f = open("e:\\test.txt", 'a')
f.write('\nwelcome to python!')
f.writelines('I love python')
f.close()

# os --- copyfile() & copy() & copytree() & move() & rmtree()
import shutil
os.makedirs('e:\\test')

shutil.copyfile('e:\\test.txt','e:\\test-copy.txt')
shutil.copytree('e:\\test','e:\\test-copy')
shutil.rmtree('e:\\test-copy')						# 空目录、有内容的目录都可以删

os.rmdir('e:\\test')								# 只能删除空目录
os.remove('e:\\copy-test.txt')

os.rename('e:\\test-copy.txt', 'e:\\copy-test.txt')	# 文件或目录都是使用这条命令

# os --- sys & local 								文件编码   REF: http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html
import sys
import locale
print sys.getdefaultencoding()						# 返回当前系统所使用的默认字符编码
print sys.getfilesystemencoding()					# 返回用于转换Unicode文件名至系统文件名所使用的编码
print locale.getdefaultlocale()						# 获取默认的区域设置并返回元组(语言, 编码)
print locale.getpreferredencoding()					# 返回用户设定的文本数据编码

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/10/3012798.html