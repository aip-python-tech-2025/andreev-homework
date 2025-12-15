class NegativeNumberError(ValueError):
    pass

def get_sum(a, b):
    return a + b


def get_div(a, b):
    WRONG_TYPE_ERROR = 1
    DIVISION_ERROR = 2

    if not (isinstance(a, int) and isinstance(b, int)):
        return None, WRONG_TYPE_ERROR

    if b == 0:
        return None, DIVISION_ERROR

    res = a // b
    return res, None


def get_mod(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return None
    finally:
        print('Посчитали результат...')


def get_sub(a, b):
    if a < b:
        raise NegativeNumberError
    return a - b


# print(get_mod(17, 3))
# print(get_mod(17, 0))

try:
    print(get_sub(17, 5))
    print(get_sub(17, 25))
except NegativeNumberError as e:
    print('Попытались вычесть из меньшего большее...')

# try:
#     a = int(input())
#     b = int(input())
#     print(a // b)
# except ZeroDivisionError:
#     print('Деление на ноль')
# except (ValueError, TypeError):
#     print('Ошибка ввода данных')
#
# print('Посчитали результат...')

# print(get_sum(a, b))
#
# res, status = get_div(a, b)
# if status == 1:
#     print('Нужно передавать только целые числа')
# elif status == 2:
#     print('Делить на ноль нельзя')
# else:
#     print(res)
