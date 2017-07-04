import threading

def hello():
    print('hello world')

t = threading.Timer(3, hello)
t.start()
