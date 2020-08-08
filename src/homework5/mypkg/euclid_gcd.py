"""Greatest common divisor."""


def euclid_gcd():
    """Поиск наибольшего общего делителя по алгоритму Евклида.

    Даны два натуральных числа. Вычислите их наибольший общий делитель при
    помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    """
    int1 = int(input("Input 1st natural number: "))
    int2 = int(input("Input 2nd natural number: "))
    saved1, saved2 = int1, int2

    if int1 < int2:
        int1, int2 = int2, int1

    while int2:
        int1, int2 = int2, int1 % int2

    return ("Greatest common divisor for {} and {} is {}"
            "".format(saved1, saved2, int1))
