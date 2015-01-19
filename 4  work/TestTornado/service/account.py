# coding=utf-8

def loginByPassword(username, password, **kwargs):
	if username == 'liguangpu@qq.com' and password == '123456':
		return True
	else:
		return False
		
if __name__ == "__main__":
	rst = loginByPassword('liguangpu@qq.com', '123456')
	print rst
	