n = int(input('Number of strings: '))
my_list = []
for i in range(n):
    my_list.append(input('Input sting: '))
print(my_list)

vow = {'a', 'e', 'i', 'o', 'u', 'y'}

for i in range(my_list):
    my_vow = set()
    my_cons = set()
    for j in range(my_list[i]):
        if j in vow: my_vow.add(item[i])
        else: my_cons.add(item[i])
    print(my_vow, my_cons)
    
