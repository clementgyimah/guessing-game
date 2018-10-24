# This is a game program that tells the user to enter a guess number.
from random import randint

random = randint(1,100)
count = 5
for i in range(5):
    user = int(input("Enter your guess: "))
    if user == random:
        print("\tCONGRATULATION!!!!!.....Correct\n")
        break
    elif 1 < user < random:
        print(" WRONG.  The number is higher than your guess\n")
    elif random < user <= 100:
        print(" WRONG.  The number is lower than your guess\n")
    elif user > 100 or user < 1:
        print("Follow simple instructions\n")
    count = count - 1
    print("You have ", count, " guesses left\n")

print("*******The number is ", random)
