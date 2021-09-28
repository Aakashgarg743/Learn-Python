import random

def start():
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome To Snake | Water | Gun Game...\n")
    comp_score = 0
    user_score = 0
    user = ""
    lives = 5

    while lives>0:
        li = ["s", "w", "g"]
        comp = random.choice(li)
        lives -= 1

        user = input("Choose one of the option listed above...\n").lower()

        if (user=="s" and comp=="s") or (user=="w" and comp=="w") or (user=="g" and comp=="g"):
            comp_score += 1
            user_score += 1
            print(f"There is a tie as you chooses {user} and computer chooses {comp} with the scores of the USER: {user_score} and COMP: {comp_score}")
            print("Total chances are left: ", lives)

        elif (user=="s" and comp=="w") or (user=="w" and comp=="g") or (user=="g" and comp=="s"):
            user_score += 1
            print(f"You win this chance as you chooses {user} and computer chooses {comp} with the scores of the USER: {user_score} and COMP: {comp_score}")
            print("Total chances are left: ", lives)

        elif (user=="w" and comp=="s") or (user=="g" and comp=="w") or (user=="s" and comp=="g"):
            comp_score += 1
            print(f"Computer win this chance as you chooses {user} and computer chooses {comp} with the scores of the USER: {user_score} and COMP: {comp_score}")
            print("Total chances are left: ", lives)
            
        else:
            print("Wrong input..")


if __name__ == '__main__':
    start()