from time import perf_counter

n = 20000000

t = perf_counter()
s = sum(range(n))
print(s, perf_counter() - t)

s = 0

t = perf_counter()
for i in range(n):
    s += i
print(s, perf_counter() - t)

l = list(range(n))
s = set(range(n))

t = perf_counter()
res = 5000000 in l
print(res, perf_counter() - t)

t = perf_counter()
res = 5000000 in s
print(res, perf_counter() - t)
