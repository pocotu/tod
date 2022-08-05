def patron(n):
    k = n -2
    for i in range (n, -1, -1):
        for j in range (k, -1, -1):
            print(" ", end="")
        k = k - 1
        for j in range (i, -1, -1):
            print("*", end="")
        print()