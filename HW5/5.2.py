count = 0
for i in range(10):
    numX = int(input('Give me a number greater then 2: '))
    if numX % 5 == 0:
        count += 1
if count == 1:
    print('1 number are divisible by 5')
else:
    print('{} numbers are divisible by 5' .format(count))
