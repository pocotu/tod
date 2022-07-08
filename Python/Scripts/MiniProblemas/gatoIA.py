import time
import random

print("Tic Tac Toe! (El Gato)\nThe positions are:\n")

print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 \n")

def tabla():
  print(' '+p[0]+' | '+p[1]+' | '+p[2]+'')
  print('---|---|---')
  print(' '+p[3]+' | '+p[4]+' | '+p[5]+'')
  print("---|---|---")
  print(' '+p[6]+' | '+p[7]+' | '+p[8]+"\n")  

pi=['1','2','3','4','5','6','7','8','9']
p=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

op1=[1,2,3,4,6,7,8,9]
op2=[5]
op3=[1,3,7,9]
op4=[2,4,6,8]

rchai=[1,3,5,7,9]

#Formas de ganar
#horizontal
wh1=[1,2,3]
vh1=[1,2,3]
wh2=[4,5,6]
vh2=[4,5,6]
wh3=[7,8,9]
vh3=[7,8,9]
Wh1=[1,2,3]
Wh2=[4,5,6]
Wh3=[7,8,9]
#vertical
wv1=[1,4,7]
vv1=[1,4,7]
wv2=[2,5,8]
vv2=[2,5,8]
wv3=[3,6,9]
vv3=[3,6,9]
Wv1=[1,4,7]
Wv2=[2,5,8]
Wv3=[3,6,9]
#diagonal
wd1=[1,5,9]
vd1=[1,5,9]
wd2=[3,5,7]
vd2=[3,5,7]
Wd1=[1,5,9]
Wd2=[3,5,7]

#Cuando gana la AI
def win():
  if wh1.count("O")==3:
    print("AI wins")
    quit()
  elif wh2.count("O")==3:
    print("AI wins")
    quit()
  elif wh3.count("O")==3:
    print("AI wins")
    quit()
  elif wv1.count("O")==3:
    print("AI wins")
    quit()
  elif wv2.count("O")==3:
    print("AI wins")
    quit()
  elif wv3.count("O")==3:
    print("AI wins")
    quit()
  elif wd1.count("O")==3:
    print("AI wins")
    quit()
  elif wd2.count("O")==3:
    print("AI wins")
    quit()
  
#Poner una X o una O
def borrar(pos,a):
  global count
  global otro
  if pos in wh1:
    wh1.remove(pos)
    vh1.remove(pos)
    wh1.append(a)
  if pos in wh2:
    wh2.remove(pos)
    vh2.remove(pos)
    wh2.append(a)
  if pos in wh3:
    wh3.remove(pos)
    vh3.remove(pos)
    wh3.append(a)
  if pos in wv1:
    wv1.remove(pos)
    vv1.remove(pos)
    wv1.append(a)
  if pos in wv2:
    wv2.remove(pos)
    vv2.remove(pos)
    wv2.append(a)
  if pos in wv3:
    wv3.remove(pos)
    vv3.remove(pos)
    wv3.append(a)
  if pos in wd1:
    wd1.remove(pos)
    vd1.remove(pos)
    wd1.append(a)
  if pos in wd2:
    wd2.remove(pos)
    vd2.remove(pos)
    wd2.append(a)
  count+=1
  if count==9:
    print("It's a draw!")
    quit()

#Movimiento de la AI
def movai(pos):
  posstr=str(pos)
  p.pop(pos-1)
  pi.remove(posstr)
  p.insert(pos-1,"O")
  pi.append("F")
  tabla()
  borrar(pos,"O")
  

#MOVIMIENTOS
#Primer movimiento del jugador
def me1():
  pos=int(input("Position: "))
  while True:
    if str(pos) in pi:
      p.pop(pos-1)
      pi.pop(pos-1)
      pi.append("F")
      p.insert(pos-1,"X")
      otro.pop(0)
      otro.insert(0,pos)
      posx.append(pos)
      posx.pop(0)
      print("\n")
      tabla()
      borrar(pos,"X")
      break
    else:
      print('Error')
      pos=int(input("Position: "))
  print("AI is thinking...")
  time.sleep(1)
  if pos in op1:
    pos=5
    movai(pos)
  elif pos in op2:
    pos=1
    movai(pos)

def me():
  win()
  pos=int(input("Position: "))
  while True:
    if str(pos) in pi:
      p.pop(pos-1)
      posstr=str(pos)
      pi.remove(posstr)
      if count==2 or count==3:
        otro.pop(1)
        otro.insert(1,pos)
      pi.append("F")
      p.insert(pos-1,"X")
      print("\n")
      tabla()
      borrar(pos,"X")
      posx.append(pos)
      break
    else:
      print('Error')
      pos=int(input("Position: "))
  print("AI is thinking...")
  time.sleep(1)
  ai()

def ai():
  pos=int(pi[0])
  if count==0:
    pos=random.choice(rchai)
  elif (wh1.count("O")==2) and len(vh1)==1:
    pos=wh1[0]
  elif (wh2.count("O")==2) and len(vh2)==1:
    pos=wh2[0]
  elif (wh3.count("O")==2) and len(vh3)==1:
    pos=wh3[0]
  elif (wv1.count("O")==2) and len(vv1)==1:
    pos=wv1[0]
  elif (wv2.count("O")==2) and len(vv2)==1:
    pos=wv2[0]
  elif (wv3.count("O")==2) and len(vv3)==1:
    pos=wv3[0]
  elif (wd1.count("O")==2) and len(vd1)==1:
    pos=wd1[0]
  elif (wd2.count("O")==2) and len(vd2)==1:
    pos=wd2[0]
  else:
    if (wh1.count("X")==2) and len(vh1)==1:
      pos=wh1[0]
    elif (wh2.count("X")==2) and len(vh2)==1:
      pos=wh2[0]
    elif (wh3.count("X")==2) and len(vh3)==1:
      pos=wh3[0]
    elif (wv1.count("X")==2) and len(vv1)==1:
      pos=wv1[0]
    elif (wv2.count("X")==2) and len(vv2)==1:
      pos=wv2[0]
    elif (wv3.count("X")==2) and len(vv3)==1:
      pos=wv3[0]
    elif (wd1.count("X")==2) and len(vd1)==1:
      pos=wd1[0]
    elif (wd2.count("X")==2) and len(vd2)==1:
      pos=wd2[0]
    else:
      if f==1 and count==4:
        if (('1' not in pi) and ('8' not in pi)) or (('9' not in pi) and ('4' not in pi)):
          if p[6]==' ':
            pos=7
        elif (('6' not in pi) and ('1' not in pi)) or (('9' not in pi) and ('2' not in pi)):
          if p[2]==' ':
            pos=3
        elif (('7' not in pi) and ('2' not in pi)) or (('3' not in pi) and ('4' not in pi)):
          if p[0]==' ':
            pos=1
        elif (('7' not in pi) and ('6' not in pi)) or (('3' not in pi) and ('8' not in pi)):
          if p[8]==' ':
            pos=9
        else:
          if p[4]==' ':
            pos=5
          elif p[2]==' ':
            pos=3
          elif p[6]==' ':
            pos=7            
          else:
            pos=int(pi[0])
      elif count==3:
        if (otro[0]==1 and otro[1]==8) or (otro[0]==8 and otro[1]==1):
          pos=7
        elif (otro[0]==1 and otro[1]==6) or (otro[0]==6 and otro[1]==1):
          pos=3
        elif (otro[0]==7 and otro[1]==2) or (otro[0]==2 and otro[1]==7):
          pos=1
        elif (otro[0]==7 and otro[1]==6) or (otro[0]==6 and otro[1]==7):
          pos=9
        elif (otro[0]==9 and otro[1]==2) or (otro[0]==2 and otro[1]==9):
          pos=3
        elif (otro[0]==9 and otro[1]==4) or (otro[0]==4 and otro[1]==9):
          pos=7
        elif (otro[0]==3 and otro[1]==4) or (otro[0]==4 and otro[1]==3):
          pos=1
        elif (otro[0]==3 and otro[1]==8) or (otro[0]==8 and otro[1]==3):
          pos=9
        elif (posx[0] in op3) and (posx[1] in op3):
          if p[1]==' ':
            pos=2
          elif p[3]==' ':
            pos=4
        else:
          if p[4]==' ':
            pos=5
          elif p[2]==' ':
            pos=3
          elif p[6]==' ':
            pos=7            
          else:
            pos=int(pi[0])
      elif count==2:
        if posx[1]==2 or posx[1]==4:
          pos=9
        elif posx[1]==6 or posx[1]==8:
          pos=1
        elif p[4]=="X":
          if p[0]=='O':
            pos=9
          elif p[2]=='O':
            pos=7
          elif p[6]=='O':
            pos=3
          elif p[8]=='O':
            pos=1
        else:
          pos=2
      else:
        if p[4]==' ':
          pos=5
        elif p[2]==' ':
          pos=3
        elif p[6]==' ':
          pos=7
        else:
          pos=int(pi[0])
  movai(pos)

otro=[0,0]
count=0
posx=[0]
f=0
while True:
  print("Who first? (¿Quién primero?)\n 1) Me\n 2) AI")
  arranca=int(input())
  if arranca==1:
    me1()
    me()
    me()
    me()
    me()
    break
  elif arranca==2:
    f=1
    ai()
    me()
    me()
    me()
    me()
    break
  else:
    print("Error")