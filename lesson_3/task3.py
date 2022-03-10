# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint


arr = [randint(0, 10) for _ in range(15)]

print(f'Массив: {arr}')

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

print(f'Минимальный элемент массива: {arr[min_index]}')
print(f'Максимальный элемент массива: {arr[max_index]}')

if min_index < max_index:
    print(f'Сумма элементов: {sum(arr[min_index + 1 : max_index])}')
else:
    print(f'Сумма элементов {sum(arr[max_index + 1 : min_index])}')
