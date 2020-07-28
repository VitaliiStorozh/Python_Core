"""Написати функцію arithmetic,
яка приймає арефметичне рівняння та повертає результат.
"""
from math import *

def arithmetic(string_operation):
    '''Do arifmetic operation'''
    return eval(string_operation)

def main():
    """Output result"""
    string_operation = input('Enter the equation to calculate: ')
    print("The result is: %d" %arithmetic(string_operation))
    
if __name__ == '__main__':
    main()
