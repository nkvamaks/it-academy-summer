"""Пары элементов.

Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def pairs_elem(string):
    """Calculate number of pairs in the input string and return this number."""
    elem_count = {}

    for elem in string.split():
        elem_count[elem] = elem_count.get(elem, 0) + 1

    pairs = sum(sum(range(1, elem_count[x])) for x in elem_count)

    return pairs
