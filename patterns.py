# PATTERN 1
def pattern(n):
    k = 2 * n - 2      # n = 10  | k = 18 or you can use simply k = n here
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 1
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
pattern(10)

# PATTERN 2
def pattern(n):
    k = n       # n = 10  | k = 18
    for i in range(n, 0, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(1, i+1):
            print("* ", end="")
        print("\r")
pattern(10)

# PATTERN 3
def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, 0, -1):
        for j in range(1, i):
            print("* ", end="")
        print("\r")
pattern(10)

# PATTERN 4
def pattern(n):
    k = 2 * n - 2
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 2
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
    k = k - 1
    for i in range(n, 0, -1):
        for j in range(k, -5, -1):
            print(end=" ")
        k = k + 2
        for j in range(1, i):
            print("* ", end="")
        print("\r")
pattern(10)

# PATTERN 5
def pattern(n):
    k = n
    for i in range(n, 0, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 1
        for j in range(1, i+1):
            print("* ", end="")
        print("\r")
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 1
        for j in range(1, i+1):
            print("* ", end="")
        print("\r")
pattern(5)

# PATTERN 6
def pattern(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i==1 and j==3) or (i==2 and j==2) or (i==3 and j==1) or (i==4 and j==2) or (i==5 and j==3) or (i==2 and j==4) or (i==3 and j==5) or (i==4 and j==4):
                print("*", end="")
            else:
                print(end=" ")
        print()
pattern(5)

# PATTERN 7
def pattern(n):
    k = 0
    for i in range(1, n+1):
        k += 1
        for j in range(1, i+1):
            print(k, end=" ")
        print()
pattern(5)

# PATTERN 8
def pattern(n):
    k = 6
    for i in range(n, 0, -1):
        k -= 1
        for j in range(1, i+1):
            print(k, end=" ")
        print()
pattern(5)

# PATTERN 9
def pattern(n):
    k = 0
    s = n
    for i in range(1, n+1):
        for j in range(1, s+1):
            print(end=" ")
        s = s - 1
        k += 1
        for j in range(1, i+1):
            print(k, end=" ")
        print()

    for i in range(n, 0, -1):
        for j in range(s, -2, -1):
            print(end=" ")
        s = s + 1
        k -= 1
        for j in range(1, i):
            print(k, end=" ")
        print()
pattern(9)

# PATTERN 10
def pattern(n):
    k = 10
    s = n
    for i in range(1, n+1):
        for j in range(1, s+1):
            print(end=" ")
        s = s - 1
        for j in range(1, i+1):
            print(k, end="")
        print()
pattern(5)

# PATTERN 11
def pattern(n):
    x = 65
    for i in range(1, n+1):
        ch = chr(x)
        x += 1
        for j in range(1, i+1):
            print(ch, end=" ")
        print("\r")
pattern(10)

# PATTERN 12
def pattern(n):
    k = n
    x = 65
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(end=" ")
        k = k - 1
        for j in  range(1, i+1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print()
pattern(10)

# PATTERN 13
def pattern(n):
    k = n
    x = 65
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(end=" ")
        k -= 1
        for j in range(1, i+1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print()
    y = 118
    for i in range(n, 0, -1):
        for j in range(k, -2, -1):
            print(end=" ")
        k += 1
        for j in range(1, i):
            ch = chr(x)
            print(ch, end=" ")
            x -= 1
        print()
pattern(8)