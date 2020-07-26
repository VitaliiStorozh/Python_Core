'''Заповнити список дійсними числами введенням з клавіатури.
Порахувати суму і добуток елементів списку.
Вивести на екран сам список, отримані суму і добуток його елементів.
'''

len_lists = int(input('Length first list(positive number): '))
while len_lists < 0:
    len_lists = int(input('Input correct number: '))

print('Input numbers for your list')
list_k = []
for i in range(len_lists):
    list_k = list_k + [int(input())]

mult = 1
for number in list_k:
    mult *= number
    
print('Your list is: \n', list_k)
print('Suma: ', sum(list_k))
print('Product: ', mult)
