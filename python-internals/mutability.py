x = 1014587934651230
s = 'hello world!'
data = [3, 1, 4]

print(type(x), type(s), type(data))
print(type(int))
print(type(type))

# Изменяемый тип данных (списки, словари, свои классы)
another = data
another.append(5)
print(data)
print(another)

print(id(data))
print(id(another))


# Неизменяемый тип данных (числа, строки, кортежи, множества)
y = x
y = y + 1
print(id(x))
print(id(y))


matrix = [[0] * 3] * 3
# matrix = [[0] * 3 for i in range(3)]
print(matrix)
print(id(matrix[0][0]))
print(id(matrix[1][0]))
print(id(matrix[2][0]))
print(id(matrix[0][1]))
print(id(matrix[1][1]))
print(id(matrix[2][1]))
matrix[0][0] = 10
print(matrix)
print(id(matrix[0][0]))
print(id(matrix[1][0]))
print(id(matrix[2][0]))
print(id(matrix[0][1]))
print(id(matrix[1][1]))
print(id(matrix[2][1]))

print(id(matrix))
print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))