cathet1 = int(input('Give me a first cathet of a right-angled triangle: '))
cathet2 = int(input('Give me a second cathet of a right-angled triangle: '))
from math import hypot
hypotenuse = hypot(cathet1, cathet2)
print('Hypotenuse is: ', hypotenuse)
