# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

n = 0


def init_n():
    global n
    n = input('Введите N: ')


def cocncate_string(str, times):
    return str * times


def sum_n():
    sum = 0
    for i in range(1, 4):
        sum += int(cocncate_string(n, i))
    return sum


init_n()
print(sum_n())
