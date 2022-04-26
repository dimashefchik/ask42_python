# Вводится строка, включающая строчные и прописные буквы.
# Требуется вывести ту же строку, заменив в ней строчные буквы прописными, а прописные – строчными.
# Например, исходная строка – "aB!cDEf", новая строка – "Ab!CdeF".
# В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру)
# и lower() (преобразование к нижнему регистру), а также методы isupper() и islower(),
# проверяющие регистр строки или символа.

text = input('Enter text: ')
print('Input text:', text)
result = ''
for letter in text:
    if letter.islower():
        result += letter.upper()
    elif letter.isupper():
        result += letter.lower()
    else:
        result += letter
print('Update text: ', result)

# Строковый метод isdigit() проверяет, состоит ли строка только из цифр.
# Напишите программу, которая запрашивает с ввода два целых числа и выводит их сумму.
# В случае некорректного ввода программа не должна завершаться с ошибкой, а должна продолжать запрашивать числа.
# Обработчик исключений try-except использовать нельзя.

while True:
    a, b = input('Enter 2 interegs: ').split()
    if not a.isdigit():
        print('1-st element not an integer')
        continue
    elif not b.isdigit():
        print('2-nd element not an integer')
        continue
    else:
        print(int(a) + int(b))
