# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import randint


def get_index(array):
    imin = array.index(min(array))
    imax = array.index(max(array))

    if imin > imax:
        return imin, imax

    return imax, imin


arr = [randint(0, 10) for _ in range(5)]

print(f'Начальный массив: {arr}')

arr[get_index(arr)[0]], arr[get_index(arr)[1]] = arr[get_index(arr)[1]], arr[get_index(arr)[0]]

print(f'Измененный массив: {arr}')
