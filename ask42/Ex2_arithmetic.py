# Напишите программу (файл arithmetic.py), которая предлагала бы пользователю решить пример 4 * 100 - 54.
# Потом выводила бы на экран правильный ответ и ответ пользователя.
# Подумайте, нужно ли здесь преобразовывать строку в число.
user_answer = input('Try to solve an example: 4 * 100 - 54 = ')
correct_answer = 4 * 100 - 54
print('Correct answer: {0}. Your answer: {1}'.format(correct_answer, user_answer))

# Запросите у пользователя четыре числа. Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую. Выведите результат на экран так, чтобы ответ содержал две цифры после запятой.
a,b,c,d = map(int,input('Input 4 numbers: ').split())
sum_first = a+b
sum_second = c +d
result = round(sum_first/sum_second,2)
print(f'Divide the sum of {a} and {b} by the sum of {c} and {d} = {result}')