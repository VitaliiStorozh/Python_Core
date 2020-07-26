'''Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
'''

from random import randint

m = int(input('Number of rows: '))
n = int(input('Number of columns: '))

a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = randint(0, 100)
        print('%4d' %a[i][j], end='')
    print()
print()

temp = []
for j in range(n):
    c = []
    for i in range(m):
        c.append(a[i][j])
    temp.append(min(c))
print('The maximum element among the minimum elements of the matrix columns: ', max(temp))
