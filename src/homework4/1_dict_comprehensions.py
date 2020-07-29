"""Dict comprehensions.

Создайте словарь с помощью генератора словарей, так чтобы его ключами были
числа от 1 до 20, а значениями кубы этих чисел.
"""


def dict_compr():
    """Return dict with integers 1-20 as keys and their cubes as values."""
    return {num: num**3 for num in range(1, 21)}


if __name__ == '__main__':
    print(dict_compr())
