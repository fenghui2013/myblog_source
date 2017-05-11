def f():
    try:
        1/1
    except Exception, e:
        print(e)
    else:
        print("hello world")

f()
