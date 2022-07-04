from random import shuffle


letters = ["a","b", "c", "d", "e", "f", "g", "h"
"i", "j", "k", "l", "m", "n", "o", "p", "q"
"r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I"
"J", "K", "L", "M", "N", "O", "P", "Q",
"R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


print("Welcome!")
digits = int(input("Enter the length required (6-12) : "))
n = int(input("Enter the number of digits required : "))

password = ""
shuffle(letters)
shuffle(num)
if digits >= 6 and digits <=12 :
  for i in range(digits - n) :
    password = password + letters[i] 
   
  for j in range(n) :
     password = password + num[j]
     

  
else :
  print("Password has to be between 6 and 12")
  
  
li = list(password)
shuffle(li)

final = ""
for k in li :
  final += k


#print(password)
print(final)