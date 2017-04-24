def makebold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'

    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'

    return wrapped

@makebold
@makeitalic
def say():
    return 'hello world'

print say()
