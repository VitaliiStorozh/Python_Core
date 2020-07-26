'''Порахувати суми кожного рядка і кожного стовпця матриці.
Доповнити її стовпцем, який містить суми елементів рядків та рядком,
елементами якого є суми елементів стовпців.
'''

from random import randint

m = int(input('Numbers of rows: '))
n = int(input('Numbers of columns: '))

a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(randint(1,100))
        print("%4d" %b[j], end='')
    a.append(b)
    print('   |', sum(b))
 
for i in range(n):
    print(" --", end='')
print()

for i in range(n):
    s = 0
    for j in range(m):
        s += a[j][i]
    print("%4d" % s, end='')
print()

