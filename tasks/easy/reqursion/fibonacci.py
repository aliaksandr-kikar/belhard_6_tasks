"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    assert fibonacci(1) == 1
    assert fibonacci(3) == 2
    assert fibonacci(6) == 8
    print('Решено!')
