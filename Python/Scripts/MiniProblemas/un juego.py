import random as rd

def tabla():
  print("+------+------+------+------+")
  print("|      |      |      |      |")
  print("|"+p[0]+"|"+p[1]+"|"+p[2]+"|"+p[3]+"|")
  print("|      |      |      |      |")
  print("+------+------+------+------+")
  print("|      |      |      |      |")
  print("|"+p[4]+"|"+p[5]+"|"+p[6]+"|"+p[7]+"|")
  print("|      |      |      |      |")
  print("+------+------+------+------+")
  print("|      |      |      |      |")
  print("|"+p[8]+"|"+p[9]+"|"+p[10]+"|"+p[11]+"|")
  print("|      |      |      |      |")
  print("+------+------+------+------+")
  print("|      |      |      |      |")
  print("|"+p[12]+"|"+p[13]+"|"+p[14]+"|"+p[15]+"|")
  print("|      |      |      |      |")
  print("+------+------+------+------+")

p=["      ","      ","      ","      ",
   "      ","      ","      ","      ",
   "      ","      ","      ","      ",
   "      ","      ","      ","      "]
acs=["w","a","s","d"]
v2o4=[2,2,2,2,2,2,2,2,2,4]
mw=[[4,5,6,7],[8,9,10,11],[12,13,14,15]]
ma=[[1,5,9,13],[2,6,10,14],[3,7,11,15]]
ms=[[8,9,10,11],[4,5,6,7],[0,1,2,3]]
md=[[2,6,10,14],[1,5,9,13],[0,4,8,12]]

def rand24():
  ceros=[]
  for v in range(16):
    if p[v]=="      ":
      ceros.append(v)
  pos=rd.choice(ceros)
  val=rd.choice(v2o4)
  p[pos]="   "+str(val)+"  "

def movw(v,v1,m,c):
  if p[v+c]=="      ":
    p[v+c]=p[v]
    p[v]="      "
    m+=1
  elif p[v+c]==p[v] and p[v]==v1:
    p[v]=int(p[v+c])*2
    if len(str(p[v]))==1:
      p[v+c]="   "+str(p[v])+"  "
    elif len(str(p[v]))==2:
      p[v+c]="  "+str(p[v])+"  "
    elif len(str(p[v]))==3:
      p[v+c]="  "+str(p[v])+" "
    elif len(str(p[v]))==4:
      p[v+c]=" "+str(p[v])+" "
    p[v]="      "
    m+=2
  return m

def selc(i,v,c):
  movs=0
  if p[v]!="      ":
    v1=p[v]
    if i==0:
      movs=movw(v,v1,movs,c)
    elif i==1:
      for j in range(2):
        movs=movw(v,v1,movs,c)
        if movs==1:
          v+=c
    elif i==2:
      for j in range(3):
        movs=movw(v,v1,movs,c)
        if movs>0 and movs<3:
          v+=c

def play():
  global win
  if win==0:
    for w in p:
      if w!="      " and int(w)==2048:
        win=1
        print("You win, just continue")
        break
  tab=p.copy()
  while True:
    ac=input("Acciones:\nW) Arriba     (up)\nA) Izquierda  (left)\nS) Abajo      (down)\nD) Derecha    (right)\n")
    ac=ac.lower()
    if ac in acs:
      break
    print("Error!")
  if ac=="w":
    for i in range(len(mw)):
      for a in range(len(mw[i])):
        v=mw[i][a]
        c=-4
        selc(i,v,c)
  elif ac=="a":
    for i in range(len(ma)):
      for a in range(len(ma[i])):
        v=ma[i][a]
        c=-1
        selc(i,v,c)
  elif ac=="s":
    for i in range(len(ms)):
      for a in range(len(ms[i])):
        v=ms[i][a]
        c=4
        selc(i,v,c)
  elif ac=="d":
    for i in range(len(md)):
      for a in range(len(md[i])):
        v=md[i][a]
        c=1
        selc(i,v,c)
  if tab==p:
    return
  rand24()
  tabla()

win=0
for i in range(2):
  rand24()
tabla()
while True:
  play()