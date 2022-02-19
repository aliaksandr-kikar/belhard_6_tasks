"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(some_text: str) -> dict:
    dict_str = {}
    for i in some_text:
        dict_str.setdefault(i, 0)
        dict_str[i] += 1
    return dict_str


print(count_char(STR_VAL))
