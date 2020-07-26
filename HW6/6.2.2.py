'''Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
Порахувати кількість двозначних чисел в ній.
'''
from random import randint

m = int(input('Number of rows: '))
n = int(input('Number of columns: '))

a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = randint(0, 999)
        print('%5d' %a[i][j], end='')
    print()
print()

count = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > 9 and a[i][j] < 100:
            count += 1

print('The quantity of two-digits numbers is: ', count)
