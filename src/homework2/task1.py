"""
Напишите программу, которая считает общую цену.

Вводится M рублей и N копеек цена, а также количество S товара.
Посчитайте общую цену в рублях и копейках за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    m_1 = m * s
    n_1 = n * s
    if n_1 >= 100:
        m_1 += n_1 // 100
        n_1 = n_1 % 100
    return '{0} rubles {1} kopecks'.format(m_1, n_1)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = int(input("Рубли: ")), int(input("Копейки: ")), int(input("Количество: "))
    print(total_sum(m, n, s))
