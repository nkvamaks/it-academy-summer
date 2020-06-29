"""
Greatest common divisor.

Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).
"""
# input two natural numbers and save their initial values
first_int = int(input("Input 1st natural number: "))
second_int = int(input("Input 2nd natural number: "))
first_saved, second_saved = first_int, second_int

if first_int < second_int:
    first_int, second_int = second_int, first_int

# Euclidian algorithm
while second_int:
    first_int, second_int = second_int, first_int % second_int

# output
print("Greatest common divisor for {} and {} is {}"
      "".format(first_saved, second_saved, first_int))
