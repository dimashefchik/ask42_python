print('Практическая работа по теме: Типы данных. Переменные')
# Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = 'No'
# Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.
big_int = var_int*3.5
# Измените значение, хранимое в переменной var_float, уменьшив его на единицу, результат свяжите с той же переменной.
var_float -= 1
# Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни к каким переменным.
print(f'var_int/var_float = {round(var_int/var_float,3)}')
print(f'big_int/var_float = {round(big_int/var_float,3)}')
# Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте операции конкатенации (+) и повторения строки (*).
var_str = var_str*2 + 'Yes'*3
# Выведите значения всех переменных.
print(f'var_int = {var_int} \n'
      f'var_float = {var_float} \n'
      f'var_str = {var_str} \n'
      f'big_int = {big_int} ')




