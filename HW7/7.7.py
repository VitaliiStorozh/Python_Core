"""7. Написати функцію date, яка приймає 3 аргументи -
день, місяць і рік. Повернути True, якщо така дата є в нашому календарі,
і False - в іншому випадку.
"""

def date(day, month, year):
    '''Recognize if date is real'''
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print(1)
        if 0 < day < 32: return True
        else: return False
    elif month == 2:
        print(2)
        if year % 400 == 0 and year % 100 == 0 and year % 4 == 0:
            if 0 < day < 30: return True
            else: return False
        elif year % 100 == 0 or year % 4:
            if 0 < day < 29: return True
            else: return False
        else: return False
    elif month in [4, 6, 9, 11]:
        print(3)
        if 0 < day < 31: return True
        else: return False
    else: return False

def main():
    """Output result"""
    a = int(input("Day: "))
    b = int(input("Month: "))
    c = int(input("Year: "))
    print(date(a, b, c))
        
if __name__ == '__main__':
    main()
