# Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список. На экран выводит их сумму, максимальное и минимальное из них.
# Для нахождения суммы, максимума и минимума воспользуйтесь встроенными в Python функциями sum(), max() и min().
import random
array = []
while len(array) < 8:
    array.append(random.randint(0, 50))
print(array)
print(f'sum = {sum(array)}, max = {max(array)}, min = {min(array)}')

# Напишите программу, которая генерирует сто случайных вещественных чисел и заполняет ими список. Выводит получившийся список на экран по десять элементов в ряд.
# Далее сортирует список с помощью метода sort() и снова выводит его на экран по десять элементов в строке.
# Для вывода списка напишите отдельную функцию, в качестве аргумента она должна принимать список.

array_2 = []
while len(array_2) < 100:
    number = random.random() * 15
    array_2.append(str(round(number, 2)))

for number in range(9):
    elem = 10 * number
    print(' \t '.join(array_2[elem:elem + 11]))
print('===================================')
array_2.sort()
for number in range(9):
    elem = number * 10
    print(' \t '.join(array_2[elem:elem + 11]))
