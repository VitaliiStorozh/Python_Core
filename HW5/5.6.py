countPos = 0
countNeg = 0
while True:
    i = int(input("Number: "))
    if i == 0:
        break
    elif i < 0:
        countNeg += 1
    else:
        countPos += 1
print('You have %d negative number and %d positive number' %(countNeg, countPos))
