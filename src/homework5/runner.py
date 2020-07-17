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


LOG_FILE = 'log.txt'

# stores 'function_name':<function_object> from imported modules
fn_fn = {fn_name: getattr(Runner, fn_name) for fn_name in dir(Runner)
         if not fn_name.startswith('__')}


def counter(function):

    def wrapper(*args, **kwargs):

        def add_one_run(fns_counts):
            if args:
                for fn_name in args:
                    fns_counts[fn_name] = fns_counts.get(fn_name) + 1
            else:
                for fn_name in fn_fn:
                    fns_counts[fn_name] = fns_counts.get(fn_name) + 1
            return fns_counts

        def write_log(fns_counts):
            temp = []
            with open(LOG_FILE, 'w') as fh:
                for key, value in fns_counts.items():
                    temp.append('{}={}'.format(key, value))
                output = '\n'.join(temp)
                fh.write(output)

        try:
            with open(LOG_FILE, 'r') as fh:
                fns_counts = {}  # dict representation of LOG_FILE
                for line in fh:
                    fn_name, count = line.strip().split('=')
                    fns_counts[fn_name] = int(count)
                fns_counts = add_one_run(fns_counts)
                write_log(fns_counts)

        except FileNotFoundError:
            fns_counts = {key: 0 for key in fn_fn}
            fns_counts = add_one_run(fns_counts)

            write_log(fns_counts)

        return function(*args, **kwargs)
    return wrapper


@counter
def runner(*args):
    """Run all functions taken as parameters / all functions as default."""
    if args:
        for func in args:
            print(fn_fn[func]())
    else:
        for func in fn_fn:
            print(fn_fn[func]())


if __name__ == '__main__':
    runner()
    # print()
    # runner('dict_compr', 'lang', 'cities')
