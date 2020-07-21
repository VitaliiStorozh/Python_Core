from random import *
numRan = randint(1, 100)
for i in range(10, 0, -1):
    guess = int(input("Guess the number from 1 to 100({} attempts): " .format(i)))
    if guess == numRan:
        print("Congratulate, you Win!")
        break
    elif guess > 100 or guess < 1:
        print("Out of range")
        continue
    elif guess > numRan:
        print('The guessed number is less')
    else :
        print('The guessed number is greater')
else:
    print("You lose, try to win again!")
