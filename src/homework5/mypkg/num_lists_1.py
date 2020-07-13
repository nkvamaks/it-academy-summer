"""Lists with numbers."""


def num_lists_1():
    """
    Манипуляция со списками чисел.

    Даны два списка чисел. Посчитайте, сколько различных чисел содержится
    одновременно как в первом списке, так и во втором.
    """
    list1 = [1, 2, 3, 5, 99, 150, 151]
    list2 = [2, 3, 4, 6, 99, 111, 112]

    set1 = set(list1)
    set2 = set(list2)
    return ('Количество различных элементов в обоих'
            ' списках - {}'.format(len(set1.intersection(set2))))
