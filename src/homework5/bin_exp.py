"""Nearest power of two.

Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def bin_exp(num):
    """Find and return nearest power of two for the given integer."""
    log = 0
    num0 = num
    while num:
        num >>= 1
        log += 1
    return log - 1 if abs(2**log - num0) >= abs(2**(log - 1) - num0) else log


if __name__ == '__main__':
    num = int(input('Enter positive integer: '))
    print('Nearest power of two for the input integer {} is: '
          '{}'.format(num, 2**bin_exp(num)))
