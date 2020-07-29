"""Lists with numbers.

Даны два списка чисел. Посчитайте, сколько различных чисел входит только в
один из этих списков.
"""


list1 = [1, 2, 3, 5, 99, 150, 151]
list2 = [2, 3, 4, 6, 99, 111, 112]

set1 = set(list1)
set2 = set(list2)
print(len(set1.symmetric_difference(set2)))
