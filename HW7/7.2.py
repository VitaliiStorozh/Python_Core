"""2. Написати функцію is_year_leap, приймає 1 аргумент - рік,
і повертає True, якщо рік високосний, і False в іншому випадку.
"""

def is_year_leap(year):
    '''Recognize year leap'''
    if year % 400 == 0 and year % 100 == 0: return True
    elif year % 100 == 0 or year % 4: return False
    else: return True

def main():
    """Output result"""
    year1 = int(input("Year: "))
    print(is_year_leap(year1))
        
if __name__ == '__main__':
    main()


