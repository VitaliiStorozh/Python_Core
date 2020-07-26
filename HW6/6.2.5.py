'''Дві матриці заповнюються введенням з клавіатури.
В елементи третьої матриці такої ж розмірності
записати більші з відповідних елементів перших двох. 
'''

m = int(input('Number of rows: '))
n = int(input('Number of columns: '))

print("Input numbers for 1 matrix: ")
a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input())

print("Input numbers for 2 matrix: ")
b = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        b[i][j] = int(input())
        
c = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j] >= b[i][j]:
            c[i][j] = a[i][j]
        else:
            c[i][j] = b[i][j]

print('First matrix')
for i in range(m):
    for j in range(n):
        print('%4d' %a[i][j], end='')
    print()
print()

print('Second matrix')
for i in range(m):
    for j in range(n):
        print('%4d' %b[i][j], end='')
    print()
print()

print('Combo-matrix with biggest element')
for i in range(m):
    for j in range(n):
        print('%4d' %c[i][j], end='')
    print()
