"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    numb_1 = 0
    numb_2 = 1
    while True:
        yield numb_2
        numb_1, numb_2 = numb_2, numb_1 + numb_2


fibonacci_gen = fibonacci()

print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
