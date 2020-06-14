"""Уникальные элементы.

Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
lst = [1, 2, 1, 3, 'a', 'b', 'cc', 'cc']
lst_unique = []  # список для сохранения уникальных элементов
dict_ = {}  # словарь для хранения элементов строки и их количества
# создаем словарь, хранящий элементы входной строки и их количества
for elem in lst:
    dict_[elem] = dict_.get(elem, 0) + 1
# сохраняем уникальные элементы в новый список и печатаем его
for elem in lst:
    if dict_.get(elem) == 1:
        lst_unique.append(elem)

print("Исходный список -", lst)
print("Уникальные элементы списка -", lst_unique)
