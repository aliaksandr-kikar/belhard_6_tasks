"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n: int) -> int:
    if n == 0:
        result = 0
        return result
    else:
        result = n % 10 + sum_of_numbers(int(n / 10))
    return result


print(sum_of_numbers(33333))
