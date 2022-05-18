# Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита.
# Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга.
# Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
from random import randint

class Warrior:
    health = 100

    def attack(self):
        self.health -= 20

war1 = Warrior()
war2 = Warrior()

print('Battle start.......')

while True:
    at = randint(1,2)

    if at == 1:
        # print('Warrior_1 attacked Warrior_2')
        war2.attack()
        if war2.health <= 0:
            print('Warrior_2 died...... \nCongratulation!!\nWarrior_1 is winner!!!')
            break
        else:
            print(f'Warrior_2 {war2.health} health left')
    else:
        # print('Warrior_2 attacked Warrior_1')
        war1.attack()
        if war1.health <= 0:
            print('Warrior_1 died...... \nCongratulation!!\nWarrior_2 is winner!!!')
            break
        else:
            print(f'Warrior_1 {war1.health} health left')

print('Battle finish.')