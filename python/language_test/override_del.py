class Life:
    def __init__(self, name='unknown'):
        print('hello %s' % name)
        self.name = name

    def __del__(self):
        print('goodbye %s' % self.name)

t = Life('tom')
t = 'xxx'
