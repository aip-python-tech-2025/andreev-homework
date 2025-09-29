print('Hello World', 8, sep='_', end='!\n')

s = 'Hello World'
print(s)

x = int(input('Введите число:'))
print(x * 5)

condition = x >= 18
print(condition)

if x >= 45:
    print('Можно')
elif condition:
    print('Спорно')
else:
    print('Нельзя')

while x < 45:
    if x == 27:
        # continue
        break
    print(x)
    x += 5
else:
    print('Ура...')

print('Идём дальше')

for x in 1, 8, 4, 3:
    print(x)

for i in range(5):
    print(i)

for i in range(6, 10):
    print(i)

for i in range(11, 20, 3):
    print(i)
