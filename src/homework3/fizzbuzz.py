"""FizzBuzz.

Программа, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет
Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и
3 и 5 - FizzBuzz.
"""

for n in range(1, 101):
    if not n % 15:
        print("FizzBuzz")
        continue
    if not n % 3:
        print("Fizz")
        continue
    if not n % 5:
        print("Buzz")
        continue
    print(n)
