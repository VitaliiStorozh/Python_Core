"""1. Написати функцію arithmetic, яка приймає 3 аргументи:
перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
Якщо третій аргумент +, додати їх; якщо -, то відняти;
* - помножити; / - розділити (перше на друге).
В інших випадках повернути рядок "Невідома операція".
"""

def arithmetic(a, b, c):
    '''Do simple arifmetic operation'''
    return eval(a+c+b)

def main():
    """Output result"""
    first_argument = input('Input the first argument of equation: ')
    second_argument = input('Input the second argument of equation: ')
    operation = input('Input the operation for equation: ')
    if operation not in "+-*/":
        print("Unknown operation")
    else:
        print("The result is: %.2f" %arithmetic(first_argument, second_argument, operation))
    
if __name__ == '__main__':
    main()
