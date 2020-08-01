"""Параметрический декоратор.

Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
"""
import sys


class TooManyErrors(Exception):
    """Raised when function fails more than num times."""


def too_many_errors(num):
    """Parametric decorator.

    :param num - number of allowed fails of decorated function.
    Raises TooManyErrors exception and exits when num is reached.
    """
    def dec(func):
        def wrapper(*args, **kwargs):
            nonlocal num
            try:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    num -= 1
                    print('***Function FAILED, remaining attempts -', num)
                    if not num:
                        raise TooManyErrors
            except TooManyErrors:
                print("***Number of attempts expired. Exit.***")
                sys.exit()
        return wrapper
    return dec


if __name__ == '__main__':
    NUM_FAILS = 5

    @too_many_errors(NUM_FAILS)
    def func():
        """Simulate function that drops down time to time."""
        from random import randint
        divis = randint(0, 2)
        print('Function Works: {}/{}={}'.format(42, divis, 42 / divis))

    while True:
        func()
