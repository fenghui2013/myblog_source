def f():
    count = 0
    while True:
        res = yield count, "xxx"
        print(res)
        if res == "quit":
            break
        count += 1
    yield "quit"


g = f()

print(g.next())
print(g.send("xxx"))
print(g.send("xxx"))
print(g.send("quit"))


def co_create(f):
    g = f()
    return g, g.next()

def co_resume(co, *args, **kwargs):
    return True, co.send(*args, **kwargs)

def co_yield(*args, **kwargs):
    yield args, kwargs
