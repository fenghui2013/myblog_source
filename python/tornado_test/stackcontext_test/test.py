import tornado
import tornado.ioloop
import tornado.stack_context

import contextlib

ioloop = tornado.ioloop.IOLoop.instance()


times = 0

def callback():
    print("run callback")
    #try:
    #    raise ValueError('except in callback')
    #except Exception as e:
    #    print('main exception: {}'.format(e))
    raise ValueError('except in callback')


def async_task():
    global times
    times += 1
    print('run async task {}'.format(times))
    ioloop.add_callback(callback=callback)

@contextlib.contextmanager
def contextor():
    print('==enter')
    try:
        yield
    except Exception as e:
        print('==handle exception')
        print('==exception {}'.format(e))
    finally:
        print('==release')

@contextlib.contextmanager
def contextor2():
    print('====enter')
    try:
        yield
    except Exception as e:
        print('====handle exception')
        print('====exception {}'.format(e))
    finally:
        print('====release')


def main():
    sc = tornado.stack_context.StackContext(contextor)
    with sc:
        async_task()
    sc2 = tornado.stack_context.StackContext(contextor2)
    with sc2:
        ioloop.call_later(5, ioloop.stop)
    ioloop.start()
    print("ioloop start ...")
    print('end')


main()
