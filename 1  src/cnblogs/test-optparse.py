# coding=utf-8
'''
from optparse import OptionParser
MSG_USAGE = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2..]"
optParser = OptionParser(MSG_USAGE)
optParser.add_option("-f","--file",action = "store",type="string",dest = "fileName")
optParser.add_option("-v","--vison", action="store_false", dest="verbose",default='gggggg',
                     help="make lots of noise [default]")
fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)
print options.fileName
print options.verbose
print options
print args
#print optParser.print_help()									# 结尾会多一个 None, None是默认没有return其他值返回的
optParser.print_help()
#optParser.print_usage()

from optparse import OptionParser
Usage = 'myprog[ -n <number>]'
parser = OptionParser()
parser.add_option('-n', type='int', dest='num', default=888, help="input num")
#options, args = parser.parse_args(['-n22'])
options, args = parser.parse_args()
print options.num
parser.print_help()
'''
from optparse import OptionParser
optParser = OptionParser()
optParser.add_option("-n","--number",action = "store",type="int",dest = "intNumber")
optParser.add_option("-v","--version", action="store_false", dest="verbose",default='gggggggg',help="no help")
options, args = optParser.parse_args()
if options.intNumber is not None:  								# 当有选项n时，则使用给出的参数值
    #num = options.intNumber
    print options.intNumber,options.verbose

else:
    for i in range(1,5):  										# 不给选项n的情况下，默认输出的是1～4
        #num = i
        print i