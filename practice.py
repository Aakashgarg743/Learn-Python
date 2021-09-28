# AGE CALCULATOR
age = input("Enter your age or birth year:\n")
isYear = False
isAge = False
if len(age)<4 and int(age)>0:
    isAge = True
elif len(age) == 4 and int(age)>1900:
    isYear = True
else:
    print("You are not born yet...")

if isAge:
    age = 2021 - int(age)
    print(f"you will be 100 years old in {age + 100}")
    interested_year = input("You want to get your age in which year??\n")
    age = int(interested_year) - age
    print(f"You will be {age} years old in {interested_year}")

if isYear:
    print(f"You will be 100 years old in {int(age) + 100} years.")

# SWAPPING
li = [1,2,3,4]
t1 = li[:]
t1.reverse()
print("Technique 1: ", t1)

t2 = li[::-1]
print("Technique 2: ", t2)

t3 = li[:]
for i in range(len(t3)//2):
    t3[i], t3[len(t3) - i - 1] = t3[len(t3) - i - 1], t3[i]
print("Technique 3: ", t3)

# NEXT PALINDROME
def next_pali(n):
    n = n + 1
    while not is_pali(n):
        n += 1
    return n

def is_pali(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    n = int(input("Enter a number to check whether a number is palindrome or not....\n"))
    if is_pali(n):
        print("This is a palindrome number..")
    else:
        print("This is not a palindrome number...")
    inpu = int(input("You want to check the next palindrome number also\nType- 1. For Yes\n2. For No\n"))
    if inpu == 1:
        print(next_pali(n))
    else:
        print("Thanks...")

# SEARCH ENGINE
def matchingWords(sentence1, sentence2):
    score = 0
    word1 = sentence1.split(" ")
    word2 = sentence2.split(" ")
    for word1 in word1:
        for word2 in word2:
            if word1.lower() == word2.lower():
                score +=1
    return score

if __name__ == '__main__':
    sentence = ["python is good", "python is best", "aakash is good", "aakash is best"]
    query = input("Please enter your query\n")
    scores = [matchingWords(query, i) for i in sentence]
    sortedScores = [score for score in sorted(zip(scores, sentence), reverse=True)]
    print(sortedScores)
    count = 0
    for score, item in sortedScores:
        if score>0:
            count += 1
            print(f"{item}: with a score of {score}")
    print(f"{count} results founds...")