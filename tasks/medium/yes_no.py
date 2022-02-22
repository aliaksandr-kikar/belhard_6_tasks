"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    new_set = set()
    for i in some_list:
        if i not in new_set:
            new_set.add(i)
            print("No")
        else:
            print("Yes")


yes_or_no([1, 83, 12, 22, 3, 44])
yes_or_no([1, 83, 12, 22, 3, 1])
