number = int(input("Number: "))

if number <= -1000 :
    print("negative number which has 4 or more characters")
elif number <= -100 :
    print("negative three-digit number")
elif number <= -10 :
    print("negative two-digit number")
elif number <= -1 :
    print("negative one-digit number")
elif number >= 1000 :
    print("positive number which has 4 or more characters")
elif number >= 100 :
    print("positive three-digit number")
elif number >= 10 :
    print("positive two-digit number")
elif number >= 1 :
    print("positive one-digit number")
else :
    print("Zero")
