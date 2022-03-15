# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

result = {

}

for digit in range(2, 10):
    result[digit] = []
    for number in range (2, 100):
        if number % digit == 0:
            result[digit].append(number)

    print(f'Для числа {digit} кратны - {len(result[digit])}. Кратные числа: {result[digit]}')
