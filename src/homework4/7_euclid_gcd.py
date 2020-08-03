"""Greatest common divisor.

Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).
"""


int1 = int(input("Input 1st natural number: "))
int2 = int(input("Input 2nd natural number: "))
int1_init, int2_init = int1, int2

if int1 < int2:
    int1, int2 = int2, int1

while int2:
    int1, int2 = int2, int1 % int2

print("Greatest common divisor for {} and {} is {}"
      "".format(int1_init, int2_init, int1))
