#!/usr/bin/python3
import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print ('i am child process (%s) and my parend is %s.' % (os.getpid(),os.getpid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

