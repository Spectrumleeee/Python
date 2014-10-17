#coding=utf-8
# test 000
print "hello world" ; print "Goodbye!"

# test 001
width=20
height=30
area=width*height
str = "ÄãºÃhello , the area is %s" %(area)
print str

# test 002
import os
cmd_shutdown="cmd.exe /k shutdown -f -s -t 100"
cmd_cancell="cmd.exe /k shutdown -a"
'''
print 'start shutdown'
os.system(cmd_shutdown)
print 'start cancell'
os.system(cmd_cancell)
'''

# test 003
import datetime
timeLimit = datetime.date.today().weekday()
# Monday = 0, then Tuesday = 1 , ... Sunday = 6
print timeLimit


