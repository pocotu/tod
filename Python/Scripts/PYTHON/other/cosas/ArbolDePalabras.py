'''
v=input("idk: ")
for y in range (len(v)+1):
    print(v[:y])
for y in range (1,len(v)+1):
    print(v[:-y])

'''

'''
x = input('Texto: ')
for i in range(len(x)+1):   
    print(x[:i])
for i in range(len(x)+1):
    print(x[:-i])
'''

'''
s = str("olalekan.. abiodun")
print(*[s[:i+3] for i in range(len(s)-2)], sep="\n")
print(*[s[:-i-1] for i in range(len(s)-3)], sep="\n")
'''

x = 'Me gusta muchos lucerito'
print('\n'.join([x[:len(x)-abs(i-len(x)+1)]for i in range((len(x)-1)*2)]))