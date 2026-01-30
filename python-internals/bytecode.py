import dis
import demo_module
import importlib.util

code = """
flag = True
if flag:
    x = 1 + 2 * 5
else:
    x = 5
print(x)
"""

obj = compile(code, '<string>', 'exec')
dis.dis(obj)

print(obj.co_consts)
print(obj.co_names)
# print(obj.co_linetable.decode())

print(importlib.util.cache_from_source('demo_module.py'))
print(demo_module.f(5))
