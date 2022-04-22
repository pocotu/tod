a = 25
for i in range(0,5):
    for j in range(0,5):
        if i == j:
            a = a + 1
        elif j == 4:
            a = a + 2
a = a + 10
print(a)

