import functools

l = [2, 5, 1, 3, 6, 8, 4]


def mycmp(x, y):
    print(x, y)
    if x>y: return 1
    if x<y: return -1
    return 0

#sorted_l = sorted(l, cmp=mycmp)
sorted_l = sorted(l, key=functools.cmp_to_key(mycmp))

print(l)
print(sorted_l)


d = [("c", 3), ("a", 1), ("e", 6)]


sorted_d = sorted(d, key=lambda x: x[1], reverse=True)

print(sorted_d)




@functools.lru_cache(maxsize=32)
def hehe(num):
    print(num)
    return num+10

l = [1, 3, 1, 3, 1, 3]
print(l)

for temp in l:
    hehe(temp)

print(hehe.cache_info())


basetwo = functools.partial(int, base=2)
print(basetwo('1111'))


@functools.singledispatch
def fun(arg, verbose=True):
    if verbose:
        print("hello, ", end="")
    print(arg)

@fun.register(list)
def _(arg, verbose=True):
    if verbose:
        print("hi, ", end="")
    for temp in arg:
        print(temp, end=" ")
    print()

fun(1)
fun("world")
fun([1, 2, 3])
