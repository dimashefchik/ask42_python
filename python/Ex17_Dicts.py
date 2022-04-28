# Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
from random import randint

school = {}

# create dictionary school:
for number_class in range(1, 6):
    school[f'{number_class}А'] = randint(25, 30)
    school[f'{number_class}Б'] = randint(25, 30)
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
school[f'{randint(1, 6)}A'] = 20
# б) в школе появился новый класс,
school.update({f'{randint(1, 5)}В': randint(25, 30)})
# с) в школе был расформирован (удален) другой класс.
school.pop(f'{randint(1, 5)}Б')
print(school)
# Вычислите общее количество учащихся в школе.
student_sum = sum([value for value in school.values()])
print(student_sum)
student_sum_2 = 0
for number in school.values():
    student_sum_2 += number
print(student_sum_2)
print('============')
# Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию,
# которая создает и возвращает новый словарь, "обратный" исходному,
# т. е. ключами являются строки, а значениями – числа.

keys_is_numbers = {1: 'dog', 2: 'cat', 3: 'mouse', 4: 'tiger', 5: 'snake'}
keys_is_string = {}
for key, value in keys_is_numbers.items():
    keys_is_string[value] = key
print(keys_is_numbers)
print(keys_is_string)
keys_is_string_2 = {value: key for key, value in keys_is_numbers.items()}
print(keys_is_string_2)
