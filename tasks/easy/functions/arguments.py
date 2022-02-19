"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    res_dict = {}
    for i in args:
        if type(i) is int:
            res_dict = {"args_sum": sum(args)}
        else:
            raise TypeError("Все позиционные аргументы должны быть целыми")
    for n in kwargs:
        if type(n) is str:
            for max_len in kwargs.values():
                max_lens = {"kwargs_max_len": len(max_len)}
        else:
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
        res_dict.update(max_lens)
        return res_dict


print(dict_from_args(*(11, 15, 4, 6, 99, 87), **{'1': "alex", '2': "all", '3': "alexkikar"}))
