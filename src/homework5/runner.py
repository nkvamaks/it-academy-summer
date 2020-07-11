"""
Функция runner.

Вызывает функции, написанные в homework4:
a. runner() – все фукнции вызываются по очереди.
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции.
"""


class Runner:
    from mypkg.dict_comprehensions import dict_compr
    from mypkg.cities import cities

    global runner
    def runner(*args):
        for func in args:
            print(dct_fn[func]())


dct_fn = {fn_name: getattr(Runner, fn_name) for fn_name in dir(Runner)
          if not fn_name.startswith('__') and fn_name != 'runner'}
runner()
runner('dict_compr', 'cities')
# for func in attrs:
#   print(attrs[func].__name__)

#print(attrs)
# print(dict_compr())
#
# print(cities('test_cities.txt'))
#
# print(dir())
