"""
Функция runner.

Вызывает функции, написанные в homework4:
a. runner() – все фукнции вызываются по очереди.
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции.
"""


class Runner:
    """Define class Runner."""

    from mypkg.cities import cities
    from mypkg.dict_comprehensions import dict_compr
    from mypkg.euclid_gcd import euclid_gcd
    from mypkg.languages import lang
    from mypkg.num_lists_1 import num_lists_1
    from mypkg.num_lists_2 import num_lists_2
    from mypkg.words import words


LOG_FILE = 'log.txt'

# stores 'function_name':<function_object> from imported modules
fn_fn = {fn_name: getattr(Runner, fn_name) for fn_name in dir(Runner)
         if not fn_name.startswith('__')}


def counter(function):
    """Store number of calls of functions in log file."""

    def wrapper(*args, **kwargs):

        def add_one_run(fns_counts):
            """Add +1 for every runned function and save result in dict."""
            if args:
                for fn_name in args:
                    fns_counts[fn_name] = fns_counts.get(fn_name, 0) + 1
            else:
                for fn_name in fn_fn:
                    fns_counts[fn_name] = fns_counts.get(fn_name, 0) + 1
            return fns_counts

        def write_log(fns_counts):
            """Write dict into a log file."""
            with open(LOG_FILE, 'w') as fh:
                output = '\n'.join(['{}={}'.format(key, value) for
                                   key, value in fns_counts.items()])
                fh.write(output)

        # Open and load log file with existing values
        try:
            with open(LOG_FILE, 'r') as fh:
                fns_counts = {}  # dict representation of LOG_FILE
                for line in fh:
                    fn_name, count = line.strip().split('=')
                    fns_counts[fn_name] = int(count)
                fns_counts = add_one_run(fns_counts)
                write_log(fns_counts)

        # Create new log file if it doesn't exist
        except FileNotFoundError:
            fns_counts = {key: 0 for key in fn_fn}
            fns_counts = add_one_run(fns_counts)
            write_log(fns_counts)

        return function(*args, **kwargs)
    return wrapper


@counter
def runner(*args):
    """Run functions taken as parameters / all functions as default."""
    if args:
        for func in args:
            print(fn_fn[func]())
    else:
        for func in fn_fn:
            print(fn_fn[func]())


if __name__ == '__main__':
    runner('cities')
    # print()
    # runner('dict_compr', 'lang', 'cities')
