'''Поміняти місцями 2-й та 4-й стовпці матриці. Результат вивести на екран'''

from random import randint

m = int(input('Numbers of rows: '))
n = int(input('Numbers of columns: '))

matrix = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = randint(1, 100)
        print('%4d' %matrix[i][j], end ='')
    print()
    
for i in range(m):
    matrix[i][1], matrix[i][3] = matrix[i][3], matrix[i][1]

print('Matrix with changed 2 and 4 columns')
for i in range(m):
    for j in range(n):
        print('%4d' %matrix[i][j], end ='')
    print()
