# Чтобы избежать изменения исходного списка, не обязательно использовать кортеж.
# Можно создать его копию с помощью метода списка copy() или взять срез от начала до конца [:].
# Скопируйте список первым и вторым способом и убедитесь, что изменение копий никак не отражается на оригинале.
array = [1, 3, 5, 10, 12]
print(id(array))
array_2 = array.copy()
print(id(array_2))
array_3 = array[:]
print(id(array_3))
print('==========')
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от -5 до 0. Для заполнения кортежей числами напишите одну функцию.
# Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество нулей. Выведите на экран третий кортеж и количество нулей в нем.

import random

first_list = []
second_list = []
while True:
    number_1 = random.randint(0, 5)
    number_2 = random.randint(-5, 0)
    first_list.append(number_1)
    second_list.append(number_2)
    if len(first_list) == 10 and len(second_list) == 10:
        first_tuple = tuple(first_list)
        second_tuple = tuple(second_list)
        break
third_tuple = first_tuple + second_tuple
print(third_tuple)
print(third_tuple.count(0))

print('==========')


first_tuple_2 = tuple([random.randint(0, 5) for x in range(10)])
second_tuple_2 = tuple([random.randint(-5, 0) for x in range(10)])
third_tuple_2 = first_tuple_2 + second_tuple_2
print(third_tuple_2)
print(third_tuple_2.count(0))