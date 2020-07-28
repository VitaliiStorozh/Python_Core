"""6. Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
і повертає True, якщо воно просте, і False - в іншому випадку.
"""

def is_prime(a):
    '''Determines whether the number is prime'''
    count = 0
    for i in range(2, a+1):
        if a%i==0: count += 1
    if count == 1: return True
    else: return False

def main():
    """Output result"""
    number = int(input('Input your number: '))
    print(is_prime(number))
    
if __name__ == '__main__':
    main()
