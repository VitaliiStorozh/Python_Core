'''Вивести на екран елементи головної діагоналі матриці та їх суму.'''

from random import randint

m = int(input('Numbers of columns and rows: '))

matrix = [[0] * m for i in range(m)]

for i in range(m):
    for j in range(m):
        matrix[i][j] = randint(1, 100)
        print('%4d' %matrix[i][j], end ='')
    print()
print()

print('Numbers from diagonal are:')
diagonal = []
for i in range(m):
    diagonal.append(matrix[i][i])
    print('%4d' %matrix[i][i], end ='')
print()
print("Suma numbers from diagonal is:", sum(diagonal))
