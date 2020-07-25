"""Greatest divisor with the power of two.

Вводится число, найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def bin_gd(num):
    """Return Greatest divisor with the power of two for the given integer."""
    import re

    pattern = r'(0*$)'
    log = len(re.search(pattern, bin(num)).group(1))
    return log


if __name__ == '__main__':
    num = int(input('Enter positive integer: '))
    print('Greatest divisor with the power of two for the input integer {} is:'
          ' {}'.format(num, 2**bin_gd(num)))
    # print('{}({})'.format(10, 2**bin_gd(10)))
    # print('{}({})'.format(16, 2**bin_gd(16)))
    # print('{}({})'.format(12, 2**bin_gd(12)))
    # print('{}({})'.format(13, 2**bin_gd(13)))
