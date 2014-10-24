# coding=utf-8

# os --- getcwd() ��ȡ��ǰĿ¼
import os
s = os.getcwd()
print 'your location', s		# windows cmd���� python test-os.py 
'''
import time
folder = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
os.makedirs(r'%s/%s'%(os.getcwd(),folder))
'''

# os --- makedirs() & rmdir()
os.makedirs("c:\\temp\\test")
os.rmdir("c:\\temp\\test")		# ע��ֻɾ����testĿ¼
os.rmdir("c:\\temp")			# �����ɾ����tempĿ¼
	
# os --- os.path.split()		��·���ֽ�ΪĿ¼�����ļ���
a,b = os.path.split("c:\\dir1\\dir2\\file.txt")
print a
print b

# os --- os.path.splitext()		�ֽ��ļ�������չ��
a,b=os.path.splitext("c:\\dir1\\dir2\\file.txt")
print a
print b

# os --- os.path.exists()
print os.path.exists("C:\\")
print os.path.exists("C:\\123\\")
print os.path.exists("C:\\123.txt")
print os.path.exists("C:\\�ػ�.bat")

# os --- os.path.isfile()
print os.path.isfile("C:\\�ػ�.bat")
print os.path.isfile("C:\\Python27")

# os --- os.path.isdir()
print os.path.isdir("C:\\�ػ�.bat")
print os.path.isdir("C:\\Python27")

# os --- os.listdir()
#print os.listdir("C:\\")

def getDirList( p ):			# ��ȡָ��Ŀ¼�µ�������Ŀ¼���б�
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

def getFileList( p ):			# ��ȡָ��Ŀ¼�������ļ����б�
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
file = open("C:\\��ǰʱ��.bat")
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
shutil.rmtree('e:\\test-copy')						# ��Ŀ¼�������ݵ�Ŀ¼������ɾ

os.rmdir('e:\\test')								# ֻ��ɾ����Ŀ¼
os.remove('e:\\copy-test.txt')

os.rename('e:\\test-copy.txt', 'e:\\copy-test.txt')	# �ļ���Ŀ¼����ʹ����������

# os --- sys & local 								�ļ�����   REF: http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html
import sys
import locale
print sys.getdefaultencoding()						# ���ص�ǰϵͳ��ʹ�õ�Ĭ���ַ�����
print sys.getfilesystemencoding()					# ��������ת��Unicode�ļ�����ϵͳ�ļ�����ʹ�õı���
print locale.getdefaultlocale()						# ��ȡĬ�ϵ��������ò�����Ԫ��(����, ����)
print locale.getpreferredencoding()					# �����û��趨���ı����ݱ���

# REF: http://www.cnblogs.com/zhoujie/archive/2013/04/10/3012798.html