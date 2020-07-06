"""
Cities.

Дан список стран и городов каждой страны. Затем даны названия городов. Для
каждого города укажите, в какой стране он находится.
Входные данные находятся в отдельном файле в директории программы. В первой
строке этого файла содержится количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны. В
следующей строке записано число M, далее идут M запросов — названия каких-то M
городов, перечисленных выше. Программа печатает страну(ы), где находится
запрошенный город.
"""

relation = dict()  # stores relations: city-country(es)
filename = 'test_cities.txt'  # input file

with open(filename) as f:
    # from input file creates a sort of database with a relation
    # city-country(es)
    for _N in range(int(f.readline())):
        country, *cities = f.readline().split()
        for city in cities:
            relation[city] = relation.get(city, []) + [country]
    print(relation)

    # prints country(s) for the input cities
    for _M in range(int(f.readline())):
        city = f.readline().strip()
        print(*relation.get(city))
