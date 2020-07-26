'''У списку випадкових цілих чисел поміняти місцями
мінімальний і максимальний елементи.
'''

from random import randint

size = int(input('What size of array? '))
while size < 0:
    size = int(input('What size of array? '))

d = []
print("Origin list:")
for i in range(size):
    d.append(randint(1, 100))
    print('%d, ' %d[i], end='')
print()

ind_min_elem = d.index(min(d))
ind_max_elem = d.index(max(d))
temp = d[ind_min_elem]
d[ind_min_elem] = d[ind_max_elem]
d[ind_max_elem] = temp

print('New changed list:')
for item in d:
    print('%d, ' %item, end = '')
