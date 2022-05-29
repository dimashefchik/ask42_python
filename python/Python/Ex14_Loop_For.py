# Заполните список случайными числами. Используйте в коде цикл for , функции range() и randint().
import random

array = []
for elem in range(0, random.randint(10, 12)):
    array.append(random.randint(0, 20))
print(array)

# Если объект range(диапазон) передать встроенной в Python функции list(), то она преобразует его к списку.
# Создайте таким образом список с элементами от 0 до 100 и шагом 17.
array_numbers = list(range(0, 101, 17))
print(array_numbers)
# В заданном списке, состоящем из положительных и отрицательных чисел, посчитайте количество отрицательных элементов.
# Выведите результат на экран.
array_2 = []
for elem in range(15):
    array_2.append(random.randint(-10, 10))
count_positive = 0
count_negative = 0
for number in array_2:
    if number < 0:
        count_negative += 1
    elif number > 0:
        count_positive += 1
print(array_2)
print(f'list contains {count_positive} positive numbers and {count_negative} negative numbers.')

# Напишите программу, которая заполняет список пятью словами, введенными с клавиатуры, измеряет длину каждого слова
# и добавляет полученное значение в другой список.Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список
# длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
array_of_words = list(input('Enter text: ').split())
array_of_len = []
for elem in array_of_words:
    array_of_len.append(len(elem))
print(array_of_words, array_of_len, sep='\n')
