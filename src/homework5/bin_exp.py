"""Ближайшая степень двойки."""


def bin_exp(num):
    """Находит ближайшую степень двойки к введенному числу."""
    log = 0
    num0 = num
    while num:
        num >>= 1
        log += 1
<<<<<<< HEAD
    return log - 1 if abs(2**log - num0) >= abs(2**(log - 1) - num0) else log
=======
    return log-1 if abs(2**log - num0) >= abs(2**(log-1) - num0) else log
>>>>>>> 9a00c8e0fe243f7a8fb2bfdd4d3596f974b0f8d1


if __name__ == '__main__':
    num = int(input('Введите целое положительное число: '))
    print('Ближайшая степень двойки к введенному числу {}: '
          '{}'.format(num, 2**bin_exp(num)))
    # print('{}({})'.format(20, 2**bin_exp(20)))
    # print('{}({})'.format(6, 2**bin_exp(6)))
    # print('{}({})'.format(13, 2**bin_exp(13)))
    # print('{}({})'.format(1, 2**bin_exp(1)))
    # print('{}({})'.format(2, 2**bin_exp(2)))
    # print('{}({})'.format(3, 2**bin_exp(3)))
    # print('{}({})'.format(15, 2**bin_exp(15)))
    # print('{}({})'.format(17, 2**bin_exp(17)))
