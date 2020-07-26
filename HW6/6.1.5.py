'''Заповнити список випадковими додатними і від’ємними цілими числами.
Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.
'''

from random import randint

home = int(input('How many numbers do you want?: '))

d = []

for i in range(home):
    d.append(randint(-100, 100))
print('Your random list: ', d)

c = []
for item in d:
    if item >= 0:
        c.append(item)

print('Your positive list:\n', c)
