import ast

# Ошибка на этапе анализа структуры кода
# x = 10 +

# Ошибка времени выполнения кода
# x = 10 / 0
# print(x)

code = ("if flag:\n"
        "       x = 1 + 2 * 5\n"
        "else:\n"
        "       x = 0\n"
        "print(x)")
tree = ast.parse(code)
print(ast.dump(tree, indent=2))
