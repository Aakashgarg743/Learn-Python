# DICTIONARY
user = input("Welcome To My Dictionary\n['python', 'pip', 'functions']\nEnter any word that are listed above to get the meaning....\n").lower()
dic = {"python": "it is a programming language..", "pip":"it is used to install packages", "funcitons": "it is a block of code that only runs when it is called..."}

if user in dic.keys():
    print(dic[user])

else:
    print("You entered wrong input...")


# FAULTY - CALCULATOR
def add(num1, num2):
    if num1=="56" and num2=="9":
        print("77")
    else:
        user = int(input("In which format you want to get your result???\nType- \n1. Decimal\n2. Integer\n"))
        if user == 1:
            val = float(num1) + float(num2)
        else:
            val = int(num1) + int(num2)
    return val

def sub(num1, num2):
    user = int(input("In which format you want to get your result???\nType- \n1. Decimal\n2. Integer\n"))
    if user == 1:
        val = float(num1) - float(num2)
    else:
        val = int(num1) - int(num2)
    return val

def mul(num1, num2):
    if num1=="45" and num2=="3":
        print("555")
    else:
        user = int(input("In which format you want to get your result???\nType- \n1. Decimal\n2. Integer\n"))
        if user == 1:
            val = float(num1) * float(num2)
        else:
            val = int(num1) * int(num2)
    return val

def div(num1, num2):
    user = int(input("In which format you want to get your result???\nType- \n1. Decimal\n2. Integer\n"))
    if user == 1:
        val = float(num1) / float(num2)
    else:
        val = int(num1) // int(num2)
    return val

if __name__=='__main__':
    n1 = input("Enter 1st number...\n")
    n2 = input("Enter 2nd number...\n")

    if n1.isdigit() and n2.isdigit():
        inpu = int(input("What operation you want to perform\nType- \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
        if inpu == 1:
            print(add(n1, n2))
        elif inpu == 2:
            print(sub(n1, n2))
        elif inpu == 3:
            print(mul(n1, n2))
        elif inpu ==4:
            print(div(n1, n2))
        else:
            print("Wrong Input...")
    else:
        print("You enter wrong input")