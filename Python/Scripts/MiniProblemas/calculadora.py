i=5 
c='jdj'
while i==5:
  fn = input('Enter the first number! ')
  op = input('Which is the operation?(* / + -))')
  sn = input('Enter the second number!')
  
  try:
    g=float(fn)
    h=float(sn)    
  except ValueError:
    c="Enter only numbers!"
    print(c)
  b=c==  "Enter only numbers!" 
  if b==False:
   
    if  op =='+': 
      r =float(fn)+float(sn)
      print('Result:'+str(r))     
    elif op == '-':
      r= float(fn)-float(sn) 
      print('Result:'+str(r))     
    elif op== '*':
      r=float(fn)* float(sn)
      print('Result:'+str(r))   
    elif op=='/':
      try:
        r= float(fn)/float(sn)
        print('Result:'+str(r)) 
      except ZeroDivisionError:
        print('Division by zero is impossible!')
        
    else :
      print('Please, enter a valid operation!')


