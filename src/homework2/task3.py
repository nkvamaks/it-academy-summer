"""
Вводится строка.

Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """
    # write your code here
    str_1 = ''
    for char in str_:  # create a new string of unique chars w/o spaces
        if (char not in str_1) and (char != ' '):
            str_1 += char
    return str_1


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку: ")
    print(sub_string(str_))
