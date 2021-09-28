# GUESS A NUMBER GAME
import random

correct_guess = random.randint(1, 50)
user_guess = 0
count = 0
while correct_guess != user_guess:
    user_guess = int(input("Enter a guess number between 1 and 50...\n"))
    if user_guess > correct_guess:
        print("Your guess is too high...")
        count += 1
    elif user_guess < correct_guess:
        print("Your guess is too low...")
        count += 1
    else:
        count += 1
        print(f"You made a correct guess in {count} guesses...\nThank You..")

# FACTORIAL
# n! = n*(n-1)(n-2)(n-3)-------1
user = int(input("Enter a number...\n"))
fact = 1
if user == 1:
    print("1")
elif user<1:
    print("Number must be positive...")
else:
    for i in range(1, user+1):
        fact = fact * i
    print(fact)

# ATM
print("Welcome To Demo ATM...")
pin = "1234"
balance = 100
choice = 3
restart = ["Y"]
while choice > 0:
    user = int(input("Please enter 4 digit pin....\n"))
    if user == 1234:
        print("You entered your pin correctly...\n")
        while restart not in ["N", "n", "No", "no"]:
            print("What you want to do???\nType 1. Check Balance\nType 2. Make a Withdrawl\nType 3. Pay in\nType 4. Return Card")
            user_option = int(input("Choose one of the options:\n"))
            if user_option == 1:
                print("Your balance is: ", balance)
                restart = input("You want to go back??")
                if restart in ["N", "n", "No", "no"]:
                    print("Thank You")
                    break
            elif user_option == 2:
                withdrawl = float(input("Enter the amount you want to withdraw...\n"))
                if withdrawl > balance:
                    print("You don't have enough balance...")
                else:
                    balance -= withdrawl
                    print("Your updated balance is: ", balance)
                    restart = input("You want to go back??")
                    if restart in ["N", "n", "No", "no"]:
                        print("Thank You")
                        break
            if user_option == 3:
                payin = int(input("Enter the amount you want to add to your balance...\n"))
                balance += payin
                print("Your updated balance is: ", balance)
                restart = input("You want to go back??")
                if restart in ["N", "n", "No", "no"]:
                    print("Thank You")
                    break
            elif user_option == 4:
                print("Please wait...")
                print("Thank You...")
                break
            else:
                print("Please enter a correct number...")
                restart = ["Y"]
    else:
        choice -= 1
        print("You entered wrong pin...")
        if choice <= 0:
            print("You don't have any chances left....")

# PYTHAGORAS THEOREM
from math import sqrt

user = int(input("Enter a number: \n"))
for i in range(1, user+1):
    for j in range(i, user):
        c_square = i**2 + j**2
        c = int(sqrt(c_square))
        if (c_square - c**2) == 0:
            print(i, j, c)