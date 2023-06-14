def fu(x):
    if x < 10:
        return x
    else:
        return fu(x//10)+fu(x%10)

print(fu(12345))