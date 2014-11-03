#coding=utf-8
def sayHello():
    print('hello, welcome to python !')

def sayBye():
	print('byebye, see you next time !~')


#任何一个python程序都可以被其他程序引用，也可以使用python命令进行执行操作，这条语句的作用就是
#告知程序此语句以下的所有程序只有在进行python命令进行执行操作时才被执行，而在被其他程序引用时不执行

if __name__ == "__main__":
	print ('This is main of module "hello.py"')
	sayHello()
	sayBye()