'''У другому списку зберегти індекси парних елементів першого списку.
Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2,
то  другий треба заповнити значеннями 1, 4, 5, 6
(або 0, 3, 4, 5 - якщо індексація починається з нуля),
оскільки саме в цих позиціях першого масиву стоять парні числа.
'''

from random import randint

home = int(input('How many numbers do you want?: '))

d = []

for i in range(home):
    d.append(randint(-100, 100))
print('Your random list: ', d)

indeven = []
for item in d:
    if item % 2 ==0:
        indeven.append(d.index(item))

print('List of evens index: ', indeven)
