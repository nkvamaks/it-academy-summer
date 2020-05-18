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
    low_number = 0
    up_number = 0
    for char in str_:
        if (ord(char) >= 65) & (ord(char) <= 90):
            up_number += 1
        if (ord(char) >= 97) & (ord(char) <= 122):
            low_number += 1
    return (low_number, up_number)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку: ")
    print(count_letters(str_))
