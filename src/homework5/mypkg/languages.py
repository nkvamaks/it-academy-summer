"""Languages."""


def lang():
    """Языки.

    Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
    языки знают все школьники и языки, которые знает хотя бы один из
    школьников.
    Входные данные находятся в отдельном файле в директории программы. В первой
    строке этого файла содержится количество школьников N. Далее идет N чисел,
    после каждого из чисел идет Mi строк, содержащих названия языков, которые
    знает i-й школьник.
    Выходные данные: в первой строке выведите количество языков, которые знают
    все школьники. Начиная со второй строки - список таких языков. Затем -
    количество языков, которые знает хотя бы один школьник, на следующих
    строках - список таких языков.
    """
    from functools import reduce

    lang_lst = []
    filename = 'test_languages.txt'

    with open(filename) as f:
        for _N in range(int(f.readline())):
            lang_lst.append([])
            for _M in range(int(f.readline())):
                language = f.readline().strip()
                lang_lst[_N].append(language)

    lang_all_know = reduce(lambda x, y: set(x) & set(y), lang_lst)
    lang_one_know = reduce(lambda x, y: set(x) | set(y), lang_lst)

    return '{}\n{}\n{}\n{}'.format(
        len(lang_all_know),
        '\n'.join(lang_all_know),
        len(lang_one_know),
        '\n'.join(lang_one_know))
