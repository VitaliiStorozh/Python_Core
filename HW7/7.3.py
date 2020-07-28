"""3. Написати функцію square, яка приймає 1 аргумент - сторону квадрата,
і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площу квадрата і діагональ квадрата.
"""

def square(a):
    '''Calculate the perimeter of the square,
    the area of the square and the diagonal of the square.'''
    from math import sqrt
    b = 4*a
    c = a**2
    d = a * sqrt(2)
    return [b, c, d]

def main():
    """Output result"""
    side = int(input('Input the side of square: '))
    print(square(side))
    
if __name__ == '__main__':
    main()
