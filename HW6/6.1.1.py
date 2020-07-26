'''Заповнити один список випадковими числами,
інший - введеними з клавіатури числами,
в третій записати суми відповідних елементів перших двох.
Вивести вміст списків на екран.
'''

from random import *

len_lists = int(input('Length first list(positive number): '))
while len_lists < 0:
    len_lists = int(input('Input correct number: '))
list1 = []
print('Our random list: ')
for i in range(len_lists):
    list1 = list1 + [randint(1, 100)]
    #print('%d, ' %list1[i], end='')
print(list1)
print()

print('Input numbers for second list')
list2 = []
for i in range(len_lists):
    list2 = list2 + [int(input())]
print('Second list is: \n', list2)
print()

list3 = []
for i in range(len_lists):
    list3 = list3 + [list1[i] + list2[i]]
print('Third list is: \n', list3)

