# Создайте файл data.txt по образцу урока. Напишите программу, которая открывает этот файл на чтение,
# построчно считывает из него данные и записывает строки в другой файл (dataRu.txt),
# заменяя английские числительные русскими, которые содержатся в списке
# (["один", "два", "три", "четыре", "пять"]), определенном до открытия файлов.

data = ['one - 1 - I', 'two - 2 - II', 'three - 3 - III', 'four - 4 - IV', 'five - 5 - V']
file_1 = open('data.txt', 'w')
for line in data:
    file_1.write(line + '\n')
file_1.close()

new_words = ["один", "два", "три", "четыре", "пять"]
nums = []
for line in open('data.txt', 'r'):
    words = line.split()
    if words[0] == 'one':
        words[0] = new_words[0]
    elif words[0] == 'two':
        words[0] = new_words[1]
    elif words[0] == 'three':
        words[0] = new_words[2]
    elif words[0] == 'four':
        words[0] = new_words[3]
    elif words[0] == 'five':
        words[0] = new_words[4]
    nums.append(' '.join(words))

file_2 = open('dataRu.txt', 'w', encoding='UTF-8')
for line in nums:
    file_2.write(line + '\n')
file_2.close()

# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.
# Напишите программу, которая подсчитывает и выводит на экран
# общую сумму чисел, хранящихся в этом файле.

from random import randint
file_3 = open('nums.txt', 'w', encoding='UTF-8')
numbers = [str(randint(2, 7))+ ' ' for x in range(7)]
file_3.writelines(numbers)
file_3.close()

def count_sum(file_name):
    file = open(f'{file_name}', 'r')
    file_numbers = file.readline()
    summa = sum([int(x) for x in list(file_numbers.split())])
    print(summa)
    file.close()
count_sum('nums.txt')

file = open(f'nums.txt', 'r')
file_numbers_2 = file.readline()
summa_2 = 0
for x in file_numbers_2:
    if x == ' ':
        continue
    else:
        summa_2 += int(x)

print(summa_2)
file.close()
