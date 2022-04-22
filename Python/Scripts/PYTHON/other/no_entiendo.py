import numpy
import time


def gains(cash, add):
  return cash + add

def cash_game(cash):
  slot = ['bananas','ananas','peach','strawberry','golden']
  slotH = [0.4,0.3,0.2,0.075,0.025]
  slotT = [100, 200, 400, 1000, 10000]
  slotD = [25, 50, 100, 250, 5000]
  a = 0
  print(f'Welcome to cash game\neach launch cost 10$\nTry to found 3 sames fruits\n')
  for i in range(len(slot)):
    print(f'{slot[i]} - 3sames {slotT[i]}$ - 2 sames {slotD[i]}$')
    time.sleep(0.6)
  print(f'1 {slot[3]} 250$ - 1 {slot[4]} 500$')
  print()
  start = input(f'Ready to play [ g ]\n-> ')
  
  while True:
    slotF = numpy.random.choice(slot, 3, p = slotH)
    b = 1
    while b > 0:
      a += 1
      slotC = numpy.random.choice(slot, 1, p = slotH)
      print(f'Launcher {a} - {cash}$\n[{slotF[0]}]-[{slotF[1]}]-[{slotF[2]}]\n')
      launcher = input(f'[  a  ] - [  s  ] - [  d  ]\n[  k  ] keep it all\n[  l  ] launch all 100$\n->')
      cash = gains(cash, -25)
      if launcher == 'l':
        cash = gains(cash, -75)
        b = 0
      elif launcher == 'a':
        slotF[0] = slotC[0]
      elif launcher == 's':
        slotF[1] = slotC[0]
      elif launcher == 'd':
        slotF[2] = slotC[0]
      elif launcher == 'k':
        cash = condition(cash, slotF, slot, slotT, slotD, a)
        a = 0
        b = 0
        False
        time.sleep(0.5)
      else:
        cash = gains(cash, 25)
        a -= 1
        print('Error')
        
def condition(cash, slotF, slot, slotT, slotD, a):
  if slotF[0] == slotF[1] == slotF[2]:
    for i in range(len(slot)):
      if slotF[0] == slot[i]:
        cash = gains(cash, slotT[i])
        print(f'You found 3 {slot[i]}, you earn {slotT[i]}$\n\n')
        return cash
        
  elif slotF[0] == slot[4] or slotF[1] == slot[4] or slotF[2] == slot[4]:
    cash = gains(cash, 500)
    print(f'You found only on {slot[4]}, you earn 500$\n\n')
    return cash
    
  elif slotF[0] == slot[3] or slotF[1] == slot[3] or slotF[2] == slot[3]:
    cash = gains(cash, 250)
    print(f'You found only on {slot[3]}, you earn 250$\n\n')
    return cash
    
  elif slotF[0] == slotF[1] or slotF[0] == slotF[2]:
    for i in range(len(slot)):
      if slotF[0] == slot[i]:
        cash = gains(cash, slotD[i])
        print(f'You found 2 sames {slot[i]}, you earn {slotD[i]}$\n\n')
        return cash
        
  elif slotF[1] == slotF[2]:
    for i in range(len(slot)):
      if slotF[1] == slot[i]:
        cash = gains(cash, slotD[i])
        print(f'You found 2 sames {slot[i]}, you earn {slotD[i]}$\n\n')
        return cash
  
  else:
    print(f'You earn nothing {cash}$\n\n')
      
    
        
            

cash_game(1000)