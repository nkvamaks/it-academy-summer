"""List practice."""

"""
1. Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""
print('Task 1:')
lst_1 = [x + y for x in 'ab' for y in 'bcd']
print(lst_1, "\n")

"""
2. Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
"""
print('Task 2:')
lst_2 = lst_1[::2]
print(lst_2, "\n")

"""
3. Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
"""
print('Task 3:')
lst_3 = [str(n) + 'a' for n in range(1, 5)]
print(lst_3, "\n")

"""
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
"""
print('Task 4:')
print(lst_3.pop(lst_3.index('2a')), "- element '2a' from list")
print(lst_3, "- remaining list", "\n")

"""
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
этого элемента не было.
"""
print('Task 5:')
lst_5 = lst_3[:]
lst_5.append('2a')
print(lst_3, "- source list")
print(lst_5, "- copied list with added element '2a'")
