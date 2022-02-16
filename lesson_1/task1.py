# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def get_sum(digit: int) -> int:
    result = 0

    while digit > 0:
        result += digit % 10
        digit //= 10

    return result


def get_comp(digit: int) -> int:
    result = 1

    while digit > 0:
        result *= digit % 10
        digit //= 10

    return result


n = int(input("Введите Ваше число: "))
print(f'Сумма цифр числа равна {get_sum(n)}')
print(f'Произведение цифр числа равно {get_comp(n)}')
