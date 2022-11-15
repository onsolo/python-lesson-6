# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов,
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

from random import randint

arr = [randint(1, 9) for n in range(15)]
number = 0


def init_number():
    global number
    number = input('Введите трехзначное число: ')


def compare_arr(arr, number):
    result = bool(0)
    for i in range(len(arr) - 2):
        if int("".join(str(x) for x in arr[i:i + 3])) == number:
            result = bool(1)
    return result


def print_compare_result(result):
    print(f'{arr} - {number} -> {result}')


init_number()
print_compare_result(compare_arr(arr, number))
