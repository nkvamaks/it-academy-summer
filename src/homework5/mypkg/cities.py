"""Cities."""


def cities():
    """Города.

    Входные данные поступают из файла 'filename' из текущей директории. В
    файле дан список стран и городов каждой страны. В первой строке этого файла
    содержится количество стран N. Далее идет N строк, каждая строка начинается
    с названия страны, затем идут названия городов этой страны. В следующей
    строке записано число M, далее идут M запросов — названия каких-то M
    городов, перечисленных выше. Программа возвращает страну(ы), где находится
    запрошенный город в виде строки.
    """
    filename = 'test_cities.txt'
    relation = dict()
    output = []

    with open(filename) as f:
        for _N in range(int(f.readline())):
            country, *cities = f.readline().split()
            for city in cities:
                relation[city] = relation.get(city, []) + [country]

        for _M in range(int(f.readline())):
            city = f.readline().strip()
            output.append(' '.join(relation[city]))
    return '\n'.join(map(str, output))
