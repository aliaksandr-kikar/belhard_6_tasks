"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    numb_1 = 1
    numb_2 = 1
    if num_count < 1:
        raise ValueError('Введите значение больше 1')

    for i in range(num_count):
        yield numb_1
        numb_1, numb_2 = numb_2, numb_1 + numb_2
