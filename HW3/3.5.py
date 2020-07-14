money = int(input("Amount of money for change: "))
if money <= 0 :
    print("Sorry, but you don't have money ):")
else :
    print("After the exchange, you will receive:")
    lesya = money // 200
    if lesya :
        print("%d banknotes of UAH 200" %lesya)
    taras = (money%200) // 100
    if taras :
        print("%d banknotes of UAH 100" %taras)
    ivan = (money%100) // 10
    if ivan :
        print("%d banknotes of UAH 10" %ivan)
    vova = (money%10)
    if vova :
        print("%d coins of UAH 1" %vova)
