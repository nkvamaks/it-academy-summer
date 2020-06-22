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
    import string
    # get rid of punctuation in the string and create a list of single words
    lst = str_.translate(str.maketrans('', '', string.punctuation)).split()
    # return longest word
    return max(lst, key=len)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку: ")
    print(longest_word(str_))
