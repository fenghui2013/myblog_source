import concurrent.futures
import time

#def f(num):
#    time.sleep(5)
#    print(num)
#    return "----{}".format(num)
#
#
#def process_main():
#    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
#        for res in executor.map(f, range(10)):
#            print(res)
#
#def thread_main():
#    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
#        for res in executor.map(f, range(10)):
#            print(res)
#
#def main2():
#    for res in map(f, range(10)):
#        print(res)
#
#if __name__ == "__main__":
#    start = time.time()
#    thread_main()
#    end = time.time()
#    print(end-start)


def callback(future):
    print(future.result())

def f(num):
    print(num)
    return "----{}".format(num)

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(10):
            future = executor.submit(f, i)
            future.add_done_callback(callback)
