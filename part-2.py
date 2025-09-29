data = [2, 8, 10, 44, 3, 'Hello', True, [3, 8, 17]]

print(data)
print(data[0])
print(data[5])

print(data[-1])
print(data[-1][2])

data[5] = 24
print(data)

# print(data[11])

print(data[3:7])
print(data[3:])
print(data[:7])
print(data[:])

print(data[3:7:2])
print(data[7:3:-1])
print(data[::-1])

data.append(5)
print(data)

print(data.pop())
print(data.pop(6))
print(data.pop(6))
print(data)

print(data + [3, 7])
print(data * 2)

print(len(data))
print(sum(data), min(data), max(data))

print(data.index(3))
print(74 in data)

print(data.count(3))

data.sort(reverse=True)
print(data)

data.reverse()
print(data)

another_data = (3, 6, 1, 7)
print(another_data)

print(another_data.index(3))
print(len(another_data),
      sum(another_data),
      min(another_data),
      max(another_data))

a, b = (7, 6)

# x = another_data[0]
# y = another_data[1]
# z = another_data[2]
# w = another_data[3]

x, y, z, w = another_data

greeting = '''Hello World!
This is my program!'''

print(greeting)

print(greeting[0])
print(greeting[-1])
print(greeting[9:17])

# greeting[0] = 'h'

print(greeting.replace('l', 'L', 2))
print(greeting.split())

# print([int(x) for x in input().split()])
print(' | '.join(greeting.split()))

print(greeting.capitalize())
print(greeting.title())
print(greeting.upper())
print(greeting.lower())

print('Hello' in greeting)

phones = {
    '242-00-00': 'Университет ИТМО',
    '555-35-35': 'Не звонить'
}

print(phones)
print(phones['242-00-00'])
print('555-35-34' in phones)

phones['555-35-34'] = 'Неизвестный номер'
print(phones)
phones['555-35-35'] = 'Кредитное бюро'
print(phones)

for key in phones:
    print(key, phones[key])
