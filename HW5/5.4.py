y = int(input("Length of rectangle: "))
z = int(input("Width of rectangle: "))
print('1'*y)
j=0
while j < z-2:
    print('1','0'*(y-2),'1', sep = '')
    j += 1
print('1'*y)
