# Напишите программу, в которой вызывается функция, запрашивающая с ввода две строки
# и возвращающая в программу результат их конкатенации. Выведите результат на экран.
def text():
    string1 = input('Enter some text: ')
    string2 = input('Enter some text: ')
    return string1+string2

f = text()
print(f)

# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
# Функция должна возвращать полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def multi():
    res = 1
    while True:
        number = float(input('Enter number: '))
        res *= number
        if res == 0:
            break
        print(f'result of multiply = {res}')

multi()