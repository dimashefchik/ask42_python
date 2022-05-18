# Напишите программу по следующему описанию:
#
# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, фамилию и квалификацию специалиста.
# Квалификация имеет значение заданное по умолчанию, равное единице.
# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …" (вместо троеточия должны выводиться имя и фамилия объекта).
# В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.
# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет нажат Enter.
# Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.

class Person:

    def __init__(self, name, surname, skill= 1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def get_information(self):
        return f'Name = {self.name}, Surname = {self.surname}, Skill = {self.skill}'

    def __del__(self):
        print(f'До свидания, мистер {self.name,self.surname}')


worker1 = Person('Vasya', 'Pupkin', 2)
worker2 = Person('Ivan', 'Ivanov', 5)
worker3 = Person('Petya', 'Sidorov', 3)

if worker1.skill < worker2.skill:
    if worker1.skill < worker3.skill:
        del worker1
    else:
        del worker3
else:
    if worker2.skill < worker3.skill:
        del worker2
    else:
        del worker3

a = input()