n=input("enter a number below 15 digits")
m=len(n)%3
if m==1:
  n="00"+n
if m==2:
  n="0"+n
a=["" for i in range(len(n))]
for i in range(len(n)):
  if n[i]=="1":
    a[i]="one"
  if n[i]=="2":
    a[i]="two"
  if n[i]=="3":
    a[i]="three"
  if n[i]=="4":
    a[i]="four"
  if n[i]=="5":
    a[i]="five"
  if n[i]=="6":
    a[i]="six"
  if n[i]=="7":
    a[i]="seven"
  if n[i]=="8":
    a[i]="eight"
  if n[i]=="9":
    a[i]="nine"
a=a[::-1]
n=n[::-1]
for i in range(len(n)-1,0,-1):
  if i%3==2 and n[i]!="0":
    print("%s hundred"%a[i],end=" ")
  if i%3==1:
    if n[i]=="1":
      if n[i-1]=="0":
        print("ten",end=' ')
      elif n[i-1]=="1":
        print("eleven",end=' ')
      elif n[i-1]=="2":
        print("twelve",end=' ')
      elif n[i-1]=="3":
        print("thirteen",end=' ')
      elif n[i-1]=="4":
        print("fourteen",end=' ')
      elif n[i-1]=="5":
        print("fifteen",end=' ')
      elif n[i-1]=="6":
        print("sixteen",end=' ')
      elif n[i-1]=="7":
        print("seventeen",end=' ')
      elif n[i-1]=="8":
        print("eighteen",end=' ')
      elif n[i-1]=="9":
        print("nineteen",end=' ')
    else:
      if n[i]=="2":
        print("twenty",end=' ')
      if n[i]=="3":
        print("thirty",end=' ')
      if n[i]=="4":
        print("forty",end=' ')
      if n[i]=="5":
        print("fifty",end=' ')
      if n[i]=="6":
        print("sixty",end=' ')
      if n[i]=="7":
        print("seventy",end=' ')
      if n[i]=="8":
        print("eighty",end=' ')
      if n[i]=="9":
        print("ninety",end=' ')
      if n[i-1]!="0" :
        print(a[i-1],end=" ")
  if i==3 and (n[i]!="0" or n[i+1]!="0" or n[i+2]!="0")  :
    print("thousand",end=' ')
  if i==6 and (n[i]!="0" or n[i+1]!="0" or n[i+2]!="0"):
    print("million",end=' ')
  if i==9 and (n[i]!="0" or n[i+1]!="0" or n[i+2]!="0"):
    print("billion",end=' ')
  if i==12 and (n[i]!="0" or n[i+1]!="0" or n[i+2]!="0"):
    print("trillion",end=" ")