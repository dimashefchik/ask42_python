# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра.
# В теле cylinder() определена функция circle(), вычисляющая площадь круга по формуле πr2.
# В теле cylinder() у пользователя спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
# которая вычисляется по формуле 2πrh, или полную площадь цилиндра.
# В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат вычислений функции circle().
from math import pi


def cylinder():
    def circle(r):
        circle_area = 2 * pi * r
        return circle_area

    radius, side_surface = map(float, input('Enter radius and side surface of cylinder: ').split())
    print('Accepted')
    answer = int(input('1-show the side surface area, 2-show the total area of the cylinder: '))
    side_area = round(circle(radius) + side_surface, 2)
    if answer == 1:
        print(f'Side surface area = {side_area}')
    elif answer == 2:
        full_area = round(side_area + 2 * circle(radius), 2)
        print(f'Side surface area = {side_area}')
        print(f'Total area = {full_area}')


cylinder()
