"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(SCHOOL_DATA: dict, name_class: str) -> dict:
    SCHOOL_DATA[name_class] = SCHOOL_DATA[name_class] + 1
    return SCHOOL_DATA


def decr_students(SCHOOL_DATA: dict, name_class: str) -> dict:
    if SCHOOL_DATA[name_class] > 0:
        SCHOOL_DATA[name_class] = SCHOOL_DATA[name_class] - 1
    return SCHOOL_DATA


def add_class(SCHOOL_DATA: dict, name_class: str) -> dict:
    SCHOOL_DATA[name_class] = 0
    return SCHOOL_DATA


def remove_class(SCHOOL_DATA: dict, name_class: str) -> dict:
    del SCHOOL_DATA[name_class]
    return SCHOOL_DATA


def calc_students(SCHOOL_DATA: dict) -> int:
    sum_students = sum(SCHOOL_DATA.values())
    return sum_students


print(school_data)
print(incr_students(school_data, '1a'))
print(decr_students(school_data, '1a'))
print(add_class(school_data, '3a'))
print(remove_class(school_data, '3a'))
print(calc_students(school_data))
