"""
Палиндром.

Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково).  Число положительное целое, произвольной длины. Задача
требует работать только с числами (без конвертации числа в строку или
что-нибудь еще)
"""


def palindrom(n):
    """Поиск палиндрома.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """
    # write your code here
    n_0 = n  # сохраняем исходное число в n_0
    pal_num = 0  # инициализируем будущее перевернутое число n

    while n:
        rest = n % 10  # сохраняем разряд единиц
        n = n // 10  # "отрезаем" один разряд справа у исходного числа
        pal_num = pal_num * 10 + rest  # формируем перевернутое число

    return True if pal_num == n_0 else False


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = int(input("Введите целое положительное число: "))
    print(palindrom(n))
