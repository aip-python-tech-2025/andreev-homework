import sys
import gc

print(gc.collect())

data = [1, 2, 3]
data.append(data)

print(data)

print(sys.getrefcount(data))
del data

print(gc.collect())

a = []
b = []
a.append(b)
b.append(a)

del a
del b

print(gc.collect())
