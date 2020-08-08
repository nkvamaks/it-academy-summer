"""Функция runner.

Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. (все станет проще когда мы изучим модули, getattr и setattr)
    a. runner() – все фукнции вызываются по очереди
    b. runner(‘func_name’) – вызывается только функцию func_name.
    c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
from mypkg.cities import cities
from mypkg.dict_comprehensions import dict_compr
from mypkg.euclid_gcd import euclid_gcd
from mypkg.languages import lang
from mypkg.num_lists_1 import num_lists_1
from mypkg.num_lists_2 import num_lists_2
from mypkg.words import words

LOG_FILE = 'log.txt'

all_funcs = {fn_name: func for fn_name, func in locals().items()
             if not fn_name.startswith('__') and callable(func)}


def counter(function):
    """Decorator that stores number of calls of 'function' in log file."""

    def wrapper(*args, **kwargs):

        def add_one_run(fns_counts):
            """Add +1 for every runned function and save result in dict."""
            if args:
                for fn_name in args:
                    fns_counts[fn_name] = fns_counts.get(fn_name, 0) + 1
            else:
                for fn_name in all_funcs:
                    fns_counts[fn_name] = fns_counts.get(fn_name, 0) + 1
            return fns_counts

        def write_log(fns_counts):
            """Write dict into a log file."""
            with open(LOG_FILE, 'wt') as fh:
                output = '\n'.join(['{}={}'.format(key, value) for
                                   key, value in fns_counts.items()])
                fh.write(output)

        try:
            with open(LOG_FILE, 'r') as fh:
                fns_counts = {}
                for line in fh:
                    fn_name, count = line.strip().split('=')
                    fns_counts[fn_name] = int(count)
                write_log(add_one_run(fns_counts))

        except FileNotFoundError:
            fns_counts = dict.fromkeys(all_funcs, 0)
            write_log(add_one_run(fns_counts))

        return function(*args, **kwargs)
    return wrapper


@counter
def runner(*args):
    """Вызывает функции, из модулей директории mypkg.

    a. runner() – все фукнции вызываются по очереди.
    b. runner(‘func_name’) – вызывается только функцию func_name.
    c. runner(‘func’, ‘func1’...) - вызывает все переданные функции.
    """
    if args:
        fn_fn = {arg: all_funcs.get(arg) for arg in args}
    else:
        fn_fn = all_funcs.copy()

    for func in fn_fn:
        print(fn_fn[func]())


if __name__ == '__main__':
    runner()
    runner('dict_compr', 'lang', 'cities')
    runner('words')
