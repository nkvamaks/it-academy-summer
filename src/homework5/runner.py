"""
Функция runner.

Вызывает функции, написанные в homework4:
a. runner() – все фукнции вызываются по очереди.
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции.
"""
from dict_comprehensions import dict_compr
from cities import cities

print(dict_compr())

print(cities('test_cities.txt'))
