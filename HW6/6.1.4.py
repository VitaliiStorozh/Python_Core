'''Випадкові числа в діапазоні від -5 до 5 розкласти на два списки:
в один помістити тільки додатні, у другий - тільки від’ємні.
Числа, рівні нулю, ігнорувати.
Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
'''

from random import randint

home = int(input('How many numbers do you want?: '))

plus = []
minuse = []
d = []

for i in range(home):
    d.append(randint(-5, 5))
    if d[i] > 0:
        plus.append(d[i])
    elif d[i] < 0:
        minuse.append(d[i])
    else:
        pass

print('Your list:\n', d)
print('Positive list:\n', plus)
print('Negative list:\n', minuse)
