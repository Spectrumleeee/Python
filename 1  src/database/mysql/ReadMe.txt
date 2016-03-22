环境准备：
方法一：(联网)
	1、ubuntu下python安装mysqldb(前提已经安装了python环境) 	
		sudo apt-get install python-mysqldb		
	
方法二：(源码包)
	1、 sudo apt-get install libmysqlclient-dev
	2、 下载 MySQL-python-1.2.5.zip (https://pypi.python.org/pypi/MySQL-python/1.2.5)
		传输到 Ubuntu系统，unzip MySQL-python-1.2.5.zip
	3、 cd MySQL-python-1.2.5   python setup.py build    sudo python setup.py install
	
测试安装成功：

	python
	import MySQLdb