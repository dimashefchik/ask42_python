# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# Это вызов функции test(). В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(), тело которой содержит команду вывода на экран слова "Положительное".
# Если число отрицательное, то вызывается функция negative(), ее тело содержит выражение вывода на экран слова "Отрицательное".

def negative(x):
    print('Negative')


def positive(x):
    print('Positive')


def test():
    number = int(input('Enter number: '))
    if number >= 0:
        positive(number)
    else:
        negative(number)


test()
