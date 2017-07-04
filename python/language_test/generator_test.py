def t(count):
    return "res=yield " + str(count)


def f():
    count = 0
    while True:
        #res = yield count, "xxx", {"hello":"world"}
        res = t(count)
        eval(res)
        if res == "quit":
            break
        count += 1
    yield "quit"


g = f()

print(g.next())
print(g.send("xxx"))
print(g.send("xxx"))
print(g.send("quit"))

_coroutines = {}

def co_create(f):
    g = f()
    _state = {
        "status": "normal",
        "first_run": True
    }
    _coroutines[g] = _state
    return g

def co_resume(co, args):
    _state = _coroutines[co]
    _state["status"] = "running"
    if _state["first_run"]:
        _state["first_run"] = False
        return True, g.next()
    return True, co.send(args)

def co_yield(co, args):
    res = yield args
    #return res
