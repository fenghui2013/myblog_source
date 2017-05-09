import functools

def add(a, b):
    return a + b

print(add(1, 2))
plus1 = functools.partial(add, 1)
print(plus1(2))
plus1_2 = functools.partial(add, 1, 2)
print(plus1_2())
plus1_2_3 = functools.partial(add, 1, 2, 3)
print(plus1_2_3())
