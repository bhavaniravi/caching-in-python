from functools import lru_cache


# 1. A simple example

@lru_cache(maxsize=32)
def add(a, b):
    return a + b


numbers = [(1, 2), (2, 3), (3, 4), (1, 2), (1, 2)]

[add(a, b)for a, b in numbers]

print (add.cache_info())


# 2. Cache invalidation example

a = [10, 11, 12, 13, 14, 15, 16]


@lru_cache(maxsize=32)
def get_item(i):
    global a
    return a[i]


for index, i in enumerate([1, 1, 1, 3, 4, 1, 1]):
    if index == 5:
        a[i] = 99
        get_item.cache_clear()
    print (index, i, get_item(i))

print (get_item.cache_info())

# 3. Caching on non-deterministic inputs


from datetime import datetime
a = [10, 10, 10, 10, 10, 10, 1000]

@lru_cache(maxsize=32)
def get_item(i):
    global a
    dt = datetime.now()
    if dt.microsecond/2 == 0:
        return a[6]
    return a[i]


for index, i in enumerate(a):
    print (index, i, get_item(index))

print (get_item.cache_info())

