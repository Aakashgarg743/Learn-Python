import datetime
print("\t\t\t\t\t\t\t\t\t\t\tWelcome To Health Management System")
names = ["aakash", "manish", "nakul"]
user = input(f"For Which Client {names} You want to store or retrieve the data: \nEnter Name: \n").lower()
if user.isalpha():
    if user=="aakash":
        print(f"Hi {user}")
        inpu = int(input("You want to lock the data or retrieve the data???\nType- \n1. Lock\n2. Retrieve\n"))
        if inpu == 1:
            inpu2 = int(input("What you want to lock\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2==1:
                diet = input("Type the diet...")
                with open("aakash_diet.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {diet}")
                    print("Success")
            else:
                exercise = input("Type the exercise...")
                with open("aakash_exercise.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {exercise}")
                    print("Success")
        else:
            inpu2 = int(input("What you want to retrieve\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2 == 1:
                with open("aakash_diet.txt", "r") as f:
                    f.read()
                    print("Success")
            else:
                with open("aakash_exercise.txt", "a") as f:
                    f.read()
                    print("Success")
    elif user=="manish":
        print(f"Hi {user}")
        inpu = int(input("You want to lock the data or retrieve the data???\nType- \n1. Lock\n2. Retrieve\n"))
        if inpu == 1:
            inpu2 = int(input("What you want to lock\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2==1:
                diet = input("Type the diet...")
                with open("manish_diet.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {diet}")
                    print("Success")
            else:
                exercise = input("Type the exercise...")
                with open("manish_exercise.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {exercise}")
                    print("Success")
        else:
            inpu2 = int(input("What you want to retrieve\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2 == 1:
                with open("mansih_diet.txt", "r") as f:
                    f.read()
                    print("Success")
            else:
                with open("manish_exercise.txt", "a") as f:
                    f.read()
                    print("Success")
    elif user=="nakul":
        print(f"Hi {user}")
        inpu = int(input("You want to lock the data or retrieve the data???\nType- \n1. Lock\n2. Retrieve\n"))
        if inpu == 1:
            inpu2 = int(input("What you want to lock\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2==1:
                diet = input("Type the diet...")
                with open("nakul_diet.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {diet}")
                    print("Success")
            else:
                exercise = input("Type the exercise...")
                with open("nakul_exercise.txt", "a") as f:
                    f.write(f"\n{datetime.datetime.now()} {exercise}")
                    print("Success")
        else:
            inpu2 = int(input("What you want to retrieve\nType- \n1. Diet.\n2. Exercise\n"))
            if inpu2 == 1:
                with open("nakul_diet.txt", "r") as f:
                    f.read()
                    print("Success")
            else:
                with open("nakul_exercise.txt", "a") as f:
                    f.read()
                    print("Success")
    else:
        print("Wrong name entered....")
else:
    print("Wrong Input!!")