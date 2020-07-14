year = int(input("Year: "))
temp = "невисокосний" if year%4 else "високосний"
century = ((year // 100) + 1) if year%100 else (year // 100)
print("It's %s year in %s century." %(temp, century))
