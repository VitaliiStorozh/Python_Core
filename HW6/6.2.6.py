'''У матриці 10x10 поміняти значення елементів у кожному рядку,
розташовані відповідно на головній та бічній діагоналях.
'''

from random import randint

a = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        a[i][j] = randint(0, 100)
        print('%4d' %a[i][j], end='')
    print()
print()

for i in range(10):
    temp = a[i][i]
    a[i][i] = a[i-10][-i-1]
    a[i-10][-i-1] = temp

print('Matrix with changed diagonals')
for i in range(10):
    for j in range(10):
        print('%4d' %a[i][j], end='')
    print()
print()
