## This decision for Gregorian calendar

year = int(input("Year: "))

'''Every year that is exactly divisible by four is a leap year
except for years that are exactly divisible by 100,
but these centurial years are leap years if
they are exactly divisible by 400. For example,
the years 1700, 1800, and 1900 are not leap years,
but the years 1600 and 2000 are.'''

if year % 400 == 0 and year % 100 == 0 :
    temp = 'a leap'
elif year % 100 == 0 or year % 4 :
    temp = 'not a leap'
else :
    temp = 'a leap'

century = ((year // 100) + 1) if year%100 else (year // 100)

print("It's %s year in %sth century." %(temp, century))
