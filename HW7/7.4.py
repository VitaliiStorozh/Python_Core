"""1. Написати функцію arithmetic, яка приймає 3 аргументи:
перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними.
Якщо третій аргумент +, додати їх; якщо -, то відняти;
* - помножити; / - розділити (перше на друге).
В інших випадках повернути рядок "Невідома операція".
"""

def season(month):
    '''Determines the season of year'''
    if month < 3 or month == 12: return 'Winter'
    if 2 < month < 6: return 'Spring'
    if 5 < month < 9: return 'Summer'
    if 8 < month < 12: return 'Autumn'
    
def main():
    """Output result"""
    month = int(input('Input the equence number of month in year: '))
    print("The season is:", season(month))
    
if __name__ == '__main__':
    main()
