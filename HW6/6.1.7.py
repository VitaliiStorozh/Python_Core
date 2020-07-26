'''У списку знайти елементи, які в ньому зустрічаються тільки один раз,
і вивести їх на екран.
'''

from random import randint

size = int(input('Size of array: '))

d = []
for number in range(size):
    d = d + [randint(1, 100)]
print('Our list:', d)
print()

print('Unique elements in list:')
for item in d:
    if d.count(item) == 1:
        print('%d, ' %item, end='')
