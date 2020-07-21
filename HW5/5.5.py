p = int(input('Star of range: '))
h = int(input('End of range(Must be grater than Start): '))
while h < p:
    print('Input corect End of range')
    h = int(input('End of range(Must be grater than Start): '))    
sumLesP = 0
multGrateH = 1
count = 0
while True:
    j = int(input("Your number: "))
    if j == p or j == h:
        break
    elif j < p:
        sumLesP += j
    elif j > h:
        multGrateH *= j
    else:
        count += 1
if multGrateH == 1:
   multGrateH = 0 
print("""Cума чисел, які менше за 'Star of range' = %d\n
Добуток чисел, які більші за 'End of range' = %d\n
Кількість чисел, що знаходяться  в діапазоні значень від 'Start' до 'End' = %d"""\
      %(sumLesP, multGrateH, count))
