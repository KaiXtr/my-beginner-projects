import random
tip="0"

print("\n\n\n\n")
print(" _     _   ____ ____")
print("| |   | | |  _ - _  |")
print("| |   | | | | | | | |")
print("| |___| | | | | | | |")
print("|  ___  | | |     | |")
print("| |   | | | |     | |")
print("\n--------KaiXtr-------")
print("\nEscolha sua área matemática\n")
print("1 - Aritmética")
print("2 - Comparações")
print("3 - Álgebra")
print("4 - Geometria\n")
while tip not in "1234":
 tip=input()

while True:
 tip=int(tip)
 inp=""
 problem=""
 caze=0
 solve=""
 nb=[]
 op="-"
 lv=0
 tm=3
 ind=0
 
 print("\nNúmero médio:")
 lv=int(input())
 print("\nQuantos Números?")
 tm=int(input())
 while ind<tm:
  nb.append(str(random.randint(lv-30,lv+30)))
  if tip!=2 or tip!=4:
   op=random.randint(0,3)
   if op==0:op="+"
   elif op==1:op="-"
   elif op==2:op="*"
   elif op==3:op="/"
  problem+=nb[ind]+op
  ind+=1
 if tip<4:
  problem=problem[:-1]
 if tip==4:
  if len(nb)==1:
   problem="Um quadrado tem lados iguais a "+str(nb[0])+"\n"
   caze=round(random.randint(1,2))
   if caze==1:problem+="Qual o seu perímetro?"
   else:problem+="Qual a sua área?"
 
 if tip!=2 and tip!=4:solve=str(round(eval(problem)))
 if tip==2:
  solve+=nb[0]
  ind=0
  for i in nb[1:]:
   ind+=1
   if solve[ind]>i:
    solve+=">"+i
   elif solve[ind]==i:
    solve+="="+i
   elif solve[ind]<i:
    solve+="<"+i
  if tip==4:
   if caze==1:solve=int(nb[0])*4
   if caze==2:solve=int(nb[0])**2
 
 ind=-10
 chk=[]
 print(problem)
 while inp.startswith("r=")==False:
  inp=input()
 if tip!=2:
  if float(inp[2:])==float(solve):
   print("Correto!")
  else:
   while ind<float(solve)+10:
    chk.append(float(solve)+ind)
    ind+=1
   if float(inp[2:]) in chk:
    print("Quase isso...")
   else:
    print("Errado...")
   print("A resposta era "+solve)
 else:
  if inp[2:]==solve:
   print("Correto!")
  else:
   print("Errado...\nA resposta era "+solve)
  print("\n\n\n\n\n\n\n")