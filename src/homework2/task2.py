"""
Найти самое длинное слово в введенном предложении.

В случае если их несколько, самое левое в строке Учтите что
в предложении есть знаки препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
    """
    # write your code here
    str_1 = ''
    for char in str_:  # убираем все не буквы и не пробелы
        if char.isalpha() or char.isspace():
            str_1 += char
    lst = str_1.split()  # отделяем каждое слово
    max_len = 0
    max_index = 0
    for index, word in enumerate(lst):  # ищем самое длинное слово
        if len(word) > max_len:
            max_index, max_len = index, len(word)
    return lst[max_index]  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку: ")
    print(longest_word(str_))
