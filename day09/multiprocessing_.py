#!/usr/bin/python3
from multiprocessing import Process
import os
##run_proc定义了一个函数，这是子进程要执行的代码
def run_proc(name):
    print ('Run child process %s (%s)...' % (name,os.getpid()))
if __name__ == '__main__':
    print ('parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print ('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
