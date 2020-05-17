import re
import os

def check(w):
 #Verifica se é uma ou várias palavras
 w=w.lower()
 if ' ' in w:
  words=[]
  wds=""
  for i in w:
   if i==' ':
    words.append(wds)
    wds=""
    continue
   wds+=i
   if i==w[len(w)-1]:
    words.append(wds)
 else:words=[w]
 
 for w in words:
  silabs=""
  slb=[""]
  vowels=['']
  consonants=['']
  ev=[]
  ec=[]
  tipo=""
  conj=0
  pers=0
  rad=""
  genr="NEUTRO"
  sing="SINGULAR"
  temp="INFINITIVO"
  modo=""
  tonc=""
  radicais=['trabalh','am','feliz']
  ind=0
  
  for i in w:
   print(i)
   print(ind)
   print(slb)
   #Sílabas, Vogais e Consoantes
   slb[len(slb)-1]+=i
   #VOGAIS
   if i in "aeiouáéíóúâêô":
    vowels.append(i)
    #ENCONTROS VOCÁLICOS
    if ind>0:
     if w[ind-1] in "aeiouáéíóúâêô":
      if w[ind-2] in "aeiouáéíóúâêô":
       ev.append(vowels[-1]+vowels[-2]+i)
      else:
       if ind!=len(w)-1:
        if w[ind-1] in slb[ind-2]:
         ev.append("h"+vowels[len(vowels)-2]+i)
        else:ev.append(vowels[len(vowels)-2]+i)
       else:ev.append(vowels[len(vowels)-2]+i)
    #SÍLABAS VOGAIS
    if ind!=len(w)-1:       
     if w[ind+1] not in "aeiouáéíóúâêôhrsnmlz":
      slb.append("")
     elif ind!=len(w)-2:
      if w[ind+2] in "aeiouáéíóúâêôh":
       if w[ind+1]!="i":
        slb.append("")
   #CONSOANTES
   else:
    consonants.append(i)
    #ENCONTROS CONSONANTAIS
    if ind>0:
     if w[ind-1] not in "aeiouáéíóúâêô":
      ec.append(consonants[len(consonants)-2]+i)
    #SÍLABAS CONSOANTES
    if i in "rslnmz":
     if ind!=len(w)-1:
      if w[ind+1] not in "aeiouáéíóúâêôh":
       slb.append("")
   ind+=1
  ind=0
  
  #Tônica
  slb=slb[::-1]
  for i in slb:
   for s in i:
    if s in "áéíóúâêô":
     tonc=ind
   ind+=1
  if tonc==0:
   tonc="OXÍTONA"
  elif tonc==1:
   tonc="PAROXÍTONA"
  elif tonc==2:
   tonc="PROPAROXÍTONA"
  slb=slb[::-1]
  ind=0
  
  #Radicais
  for i in radicais:
   if re.search(i,w,re.I):
    rad=radicais[ind]
    break
   ind+=1
  
  #Pessoa
  pers=w.replace(rad,'')
  if w.endswith("o"):
   pers=1
  elif w.endswith("a"):
   pers=2
  if w.endswith("mos"):
   pers=1
  elif w.endswith("eis"):
   pers=2
  elif w.endswith("m"):
   pers=3
  
  #Conjugação e quantia
  if w.endswith("r"):
   temp="INFINITIVO"
   pers=1
   if w[-2]=="a":
    conj=1
   elif w[-2]=="e":
    conj=2
   elif w[-2]=="i":
    conj=3
  if w.endswith("s"):
    sing="PLURAL"
  
  #Organização de listas
  vg=[]
  cs=[]
  del(vowels[0])
  del(consonants[0])
  for i in vowels:
   if i not in vg:vg.append(i)
  for i in consonants:
   if i not in cs:cs.append(i)
  vg.sort()
  cs.sort()
  for i in slb:
   silabs+=i.upper()+"-"
  
  #Mostra as informações
  print()
  print(silabs[:-1])
  print(tonc)
  print()
  print("LETRAS: "+str(len(w)))
  if len(vg)>1:
   print(str(len(vg))+" VOGAIS: "+str(vg)[1:-1])
  if len(vg)==1:
   print("VOGAL: "+vg[0])
  if len(cs)>1:
   print(str(len(cs))+" CONSOANTES: "+str(cs)[1:-1])
  if len(cs)==1:
   print("CONSOANTE: "+cs[0])
  print()
  if len(ev)>1:
   print(str(len(ev))+" ENCONTROS VOCÁLICOS:")
  if len(ev)==1:
   print("ENCONTRO VOCÁLICO:")
  for i in ev:
   if i.startswith("h"):
    print(" HIATO - "+i[1:])
   elif len(i)==2:
    print("  DITONGO - "+i)
   elif len(i)==3:
    print("  TRITONGO - "+i)
  print()
  if len(ec)>1:
   print(str(len(ec))+" ENCONTROS CONSONANTAIS:")
  if len(ec)==1:
   print("ENCONTRO CONSONANTAl:")
  for i in ec:
   print("  "+i)
  print()
  print(str(conj)+"a CONJUGAÇÃO")
  print(str(pers)+"a PESSOA")
  print()
  print("RADICAL: "+rad)
  print("GÊNERO: "+genr)
  print("TEMPO: "+temp)
  print("QUANTIA: "+sing)
  print("MODO: "+modo)
  print("\n\n\n")

check('Infelizmente')

while True:
 print("Escreva uma palavra")
 word=input(">")
 os.system('cls')
 check(word)