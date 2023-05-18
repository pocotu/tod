import time

def codigo_1(numero):
    a = 0
    for j in range(1, numero+1):
        a += a + j

    for k in range(numero, 0, -1):
        a -= 1
        a *= 2
    return a

t0 = time.time()

primero = codigo_1(10)

t1 = time.time()

print("{}".format(t1-t0))