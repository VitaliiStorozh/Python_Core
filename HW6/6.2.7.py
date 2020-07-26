'''Змінити послідовність стовпців матриці так,
щоб елементи її першого рядка були відсортовані за зростанням.
'''

from random import randint

m = int(input('Numbers of rows: '))
n = int(input('Numbers of columns: '))

matrix = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        matrix[i][j] = randint(1, 100)
        print('%4d' %matrix[i][j], end ='')
    print()

k = n-1
while k > 0:
    ind = 0
    for j in range(k+1):
        if matrix[0][j] > matrix[0][ind]:
            ind = j
    for i in range(m):
        temp = matrix[i][ind]
        matrix[i][ind] = matrix[i][k]
        matrix[i][k] = temp
    k -= 1
        

print('Sorted matrix')
for i in range(m):
    for j in range(n):
        print('%4d' %matrix[i][j], end ='')
    print()
