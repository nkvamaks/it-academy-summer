"""Уникальные элементы.

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
lst = [1, 2, 1, 3, 'a', 'b', 'cc', 'cc']
lst_unique = []
dict_ = {}  # stores element:count

for elem in lst:
    dict_[elem] = dict_.get(elem, 0) + 1

print("Source list of elements -", *lst)
print('Unique elements -', *filter(lambda x: dict_[x] == 1, dict_))
