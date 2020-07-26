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
    c = sum(b)
    b.append(c)
    a.append(b)
    print()

temp = []
for i in range(n):
    s = 0
    for j in range(m):
        s += a[j][i]
    temp.append(s)
temp.append(0) # Add '0' for good output in table.
a.append(temp)

for i in range(m+1):
    for j in range(n+1):
        print('%4d' %a[i][j], end='')
    print()
