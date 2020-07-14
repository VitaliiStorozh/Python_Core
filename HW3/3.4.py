area = float(input("Hall's area(S) is: "))
radius = float(input("Stage's radius(R) is: "))
aisle = float(input("Aisle width(K) is: "))
from math import sqrt

if aisle*2 <= (sqrt(area) - (2*radius) ) :
    print("The stage can be located in this hall")
else :
    print("You should find another stage or hall")
