import sys

data = [1, 2, 7]
another = data
another.append(3)

another = [4, 6, 7]

data = another
print(data is another)

del data

print(sys.getrefcount(another))

x = 10
y = x
y += 1
print(x is y)
