#from multiprocessing import Process
import time
import random
#
#def f(name):
#    time.sleep(10)
#    print('hello', name)
#
#if __name__ == "__main__":
#    p = Process(target=f, args=('bob',))
#    p.start()
#    p.join()


#import multiprocessing as mp
#
#def foo(q):
#    time.sleep(100)
#    q.put("hello")
#
#if __name__ == "__main__":
#    mp.set_start_method("forkserver")
#    q = mp.Queue()
#    p = mp.Process(target=foo, args=(q,))
#    p.start()
#    p1 = mp.Process(target=foo, args=(q,))
#    p1.start()
#    p2 = mp.Process(target=foo, args=(q,))
#    p2.start()
#    p.join()
#    p1.join()
#    p2.join()
#    print(q.get())


#from multiprocessing import Process, Pipe
#
#def f(conn):
#    conn.send("hello world")
#    conn.close()
#
#if __name__ == "__main__":
#    parent_conn, child_conn = Pipe()
#    p = Process(target=f, args=(child_conn,))
#    p.start()
#    print(parent_conn.recv())
#    p.join()


#from multiprocessing import Process, Lock
#
#def foo(l, i):
#    time.sleep(random.randint(1, 5))
#    l.acquire()
#    try:
#        print("hello, {}".format(i))
#    finally:
#        l.release()
#
#
#if __name__ == "__main__":
#    lock = Lock()
#
#    for num in range(10):
#        Process(target=foo, args=(lock, num,)).start()


#from multiprocessing import Process, Value, Array
#
#def f(n, a):
#    n.value = 3.14
#    for i in range(len(a)):
#        a[i] = -a[i]
#
#if __name__ == "__main__":
#    num = Value('d', 0.0)
#    arr = Array('i', range(10))
#
#    p = Process(target=f, args=(num, arr,))
#    p.start()
#    p.join()
#
#    print(num.value)
#    print(arr[:])


from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    time.sleep(3)
    return x*x

def callback(cb_args):
    print("========== {}".format(cb_args))

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        #print(pool.map(f, range(10)))
        #for i in pool.imap_unordered(f, range(10)):
        #    print(i)

        res = pool.apply_async(f, (20,))
        #print(res.get(timeout=5))

        res = pool.apply_async(os.getpid, (), callback=callback)
        #print(res.get(timeout=1))

        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        res = pool.apply_async(time.sleep, (10, ))
        try:
            res.get(timeout=1)
        except TimeoutError:
            print("TimeoutError")

        print('xxx')

    print('end')
