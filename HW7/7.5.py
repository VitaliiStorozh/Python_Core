"""5. Користувач робить внесок в розмірі n гривень
строком на years років під 10% річних
(щороку розмір його внеску збільшується на 10%.
Ці гроші додаються до суми вкладу,
і на них в наступному році теж будуть відсотки).
Написати функцію bank, яка приймає аргументи n і years,
і повертає суму, яка буде на рахунку користувача
"""

def bank(n, years):
    '''Count deposit'''
    for i in range(1, years+1):
        n *= 1.1
        if i == 1:
            print('After %d year you will have %2.f$' %(i, n))
        else:
            print('After %d years you will have %2.f$' %(i, n))
    return n

def main():
    n = int(input("Amount of $: "))
    years = int(input("Number of years: "))
    print('In the end on your accaunt will be: %.2f$' %bank(n, years))

if __name__ == '__main__':
    main()
