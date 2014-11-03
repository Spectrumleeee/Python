#coding=utf-8
# 测试导入其它 *.py 模块 && __main__
import sys;
#dir = 'D:\\Documents and Settings\\Documents\\GitHub\\Python\\1  src\\163\\abc\\def'
dir = r'D:\Documents and Settings\Documents\GitHub\Python\1  src\163\abc\ghi'
if not dir in sys.path:
    sys.path.append(dir) 									# 加载dir目录下的所有的 *.py 模块
'''	
if not 'hi' in sys.modules:
    b = __import__('hi')
else:
    eval('import hi')
    hi = eval(reload(hi))
'''
import hi 
print hi.__name__
hi.sayHello()
hi.sayBye()

import hii
print hii.__name__
hii.sayHello()
hii.sayBye()
