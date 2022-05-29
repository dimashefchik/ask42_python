# Присвойте двум переменным любые числовые значения.
from random import randint
first_number = randint(0, 50)
second_number = randint(0, 50)
string = 'try it'
# Используя переменные из п. 1, с помощью оператора and составьте два сложных логических выражения, одно из которых дает истину, другое – ложь.
print(0 <= first_number <= 50 and 0 <= first_number <= 50 and first_number + second_number <= 100)
print(first_number < 25 and first_number >= second_number and first_number + second_number > 100)

# Аналогично выполните п. 2, но уже с оператором or.
print(first_number + second_number < second_number*4  or second_number > 0 or first_number**2 > 40)
print(first_number + second_number > 100 or second_number < 0 or first_number > 55)
# Попробуйте использовать в логических выражениях переменные строкового типа. Объясните результат.
# print(first_number > string)  >>>>>>> TypeEror ( нельзя стравнивать разные типы данных между собой)

# Напишите программу, которая запрашивала бы у пользователя два числа и выводила бы True или False в зависимости от того, больше первое число второго или нет.
a,b = map(int,input('Enter 2 numbers: ').split())
print(a>b)