"""
Функция runner.

Вызывает функции, написанные в homework4:
a. runner() – все фукнции вызываются по очереди.
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции.
"""


class Runner:
    """Define class Runner."""

    from mypkg.dict_comprehensions import dict_compr
    from mypkg.cities import cities
    from mypkg.num_lists_1 import num_lists_1
    from mypkg.num_lists_2 import num_lists_2
    from mypkg.languages import lang
    from mypkg.words import words
    from mypkg.euclid_gcd import euclid_gcd

    global runner

    def runner(*args):
        """Run all functions taken as parameters / all functions as default."""
        if args:
            for func in args:
                print(dct_fn[func]())
        else:
            for func in dct_fn:
                print(dct_fn[func]())


# stores 'function_name':<function_object>
dct_fn = {fn_name: getattr(Runner, fn_name) for fn_name in dir(Runner)
          if not fn_name.startswith('__') and fn_name != 'runner'}

if __name__ == '__main__':
    # runner()
    # print()
    runner('lang')
