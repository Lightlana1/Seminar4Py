# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
lst = [randint(-10, 10) for i in range(20)]
print(lst)
lst2 = []
for i in range(len(lst)):
    if lst[i] not in lst2:
        lst2.append(lst[i])
print(lst2)
