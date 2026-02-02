import time
from concurrent.futures import ThreadPoolExecutor

def cpu_task(n: int) -> int:
    s = 0
    for i in range(n):
        s += i*i
    return s

N = 2_000_000
t0 = time.perf_counter()
for _ in range(20):
    cpu_task(N)
print("последовательно:", round(time.perf_counter() - t0, 3), "сек")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=10) as ex:
    list(ex.map(cpu_task, [N] * 20))
print("10 потоков:", round(time.perf_counter() - t0, 3), "сек")