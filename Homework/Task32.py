# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и
# не больше заданного максимума)

from random import randint
n = int(input("Введите количество элементов массива: "))
numbers = [randint(1, 20) for i in range(n)]
print(numbers)
min_bound = int(input("Введите min: "))
max_bound = int(input("Введите max: "))
indexes = [i for i in range(n) if min_bound <= numbers[i] <= max_bound]
print("Индексы эл-в в заданном диапазоне:", *indexes)
