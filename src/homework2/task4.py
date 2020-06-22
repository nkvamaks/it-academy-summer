"""Подсчет строчных и прописных букв.

Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.
"""


def count_letters(str_):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество пописных.
    """
    # write your code here
    low_number = sum((1 for char in str_ if char.islower()))
    up_number = sum((1 for char in str_ if char.isupper()))
    return (low_number, up_number)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку: ")
    print(count_letters(str_))
