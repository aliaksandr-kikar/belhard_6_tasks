"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 120
"""


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(0) == 1
    print('Решено!')
