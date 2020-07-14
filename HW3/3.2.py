shape = input("Which Geometric shape's area you need? Rectangle - r, triangle - t, disk - d: ")
if shape == 'r' :
    length = float(input("Length of your rectangle: "))
    width = float(input("Width of your rectangle: "))
    area = length * width
    print("Area of your rectangle is: %d" %area)
elif shape == 't' :
    height = float(input("Height of your triangle: "))
    length = float(input("The length of the base of your triangle: "))
    area = (height*length) / 2
    print("Area of your rectangle is: %d" %area)
elif shape == 'd' :
    from math import pi
    radius = float(input("Radius of your disk: "))
    area = pi * (radius ** 2)
    print("Area of your disk is: %d" %area)
else:
    print('Wrong mining!')
