'''
this script demonstrates that using multiporcessing.Lock essentially
turns the parallel processing in to serial processing (much slower).
'''

from multiprocessing import Process, Lock
import time

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
        time.sleep(1)
        print('hello world', i)
    finally:
        l.release()

def f2(i):
    print('hello world', i)
    time.sleep(1)
    print('hello world', i)

if __name__ == '__main__':

    print('multiprocessing with lock ...')
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
    

    time.sleep(10)
    print('multiprossing without lock ...')
    for num in range(10):
        Process(target=f2, args=(num, )).start()
    
    time.sleep(10)
    print('multiprossing with join')
    for num in range(10):
        p = Process(target=f2, args=(num, ))
        p.start()
        p.join()
    