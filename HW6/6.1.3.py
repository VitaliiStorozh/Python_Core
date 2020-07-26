'''Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4,
записати їх в список. Порахувати кількість додатних,
від’ємних і нульових елементів.
Вивести на екран елементи списку і пораховані кількості.
'''
from random import randint

plus = 0
minuse = 0
zero = 0
d = []
print('Your list: ')
for i in range(20):
    d.append(randint(-4, 5))
    print('%d, ' %d[i], end='')
    if d[i] > 0:
        plus += 1
    elif d[i] < 0:
        minuse += 1
    else:
        zero += 1
print()

print('List include %d positive, %d negative and %d zero elements'\
      %(plus, minuse, zero))
