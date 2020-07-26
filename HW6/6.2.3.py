'''Матриця 5x4 заповнюється введенням з клавіатури
(крім останніх елементів рядків).
Програма повинна обчислювати суму введених елементів кожного рядка
і записувати її в останній рядок. Наприкінці слід вивести отриману матрицю.
'''

m = 5
n = 4
a = []

for i in range(m):
    b = []
    for j in range(n-1):
        b.append(int(input("Input numbers for matrix: ")))
    b.append(sum(b))
    a.append(b)

for i in range(m):
    for j in range(n):
        print('%4d' %a[i][j], end='')
    print()
