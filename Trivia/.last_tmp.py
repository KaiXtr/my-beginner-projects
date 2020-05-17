import datetime
import random
import time

a=''
r=0
i=0
ind=0
ix=0
player=0
players=1
yn='@'
#Itens
sc=[]
md=[]
gw=[]
bar=[]
cc=[]
sp=[1]
fh=3
#Listas de Perguntas
qgk=[]
qcm=[]
qlt=[]
qmc=[]
qhs=[]
qcc=[]
ctg=['1','2','3','4','5','6']
#Estatísticas
nm=[]
qst=[]
ac=0
er=0
mode='0'
tempo=0
pastime=0
folder='storage/emulated/0/Trivia/'

fileopen=open(folder+'UserData.db','r')
while True:
    i=fileopen.readline()[:-1]
    if i.startswith('H'):
        pastime=int(i[1:])
        break
    else:
        nm.append(i)
        sc.append(int(fileopen.readline()[:-1]))
        md.append(int(fileopen.readline()[:-1]))
        gw.append(int(fileopen.readline()[:-1]))
fileopen.close()

fileopen=open(folder+'Trophies.db','r')
while True:
    i=fileopen.readline()[:-1]
    if i=='':break
    else:qst.append([int(i[:3]),i[3:]])
fileopen.close()

files=['Tecnologia.txt','Cinema.txt','Literatura.txt','Música.txt','História.txt','Ciências.txt']
for t in files:
    lis=[]
    fileopen=open(folder+t,'r')
    while True:
        i=fileopen.readline()
        if i=='':
            break
        elif i.startswith('?'):
            lis.append([])
            lis[ind].append(i[1:-1])
        elif i.startswith('>'):
            lis[ind].append(i[:-1])
        elif i.startswith('X'):
            lis[ind].append(i[:-1])
        elif i.startswith('!'):
            lis[ind].append(i[1:-1])
        elif i=='-\n':
            ind+=1
    fileopen.close()
    if t=='Tecnologia.txt':qgk=lis
    if t=='Cinema.txt':qcm=lis
    if t=='Literatura.txt':qlt=lis
    if t=='Música.txt':qmc=lis
    if t=='História.txt':qhs=lis
    if t=='Ciências.txt':qcc=lis
    ind=0
i=1
lis=[]

def instructions():
    print('Para se jogar é bem simples:')
    time.sleep(2)
    print('- Será sorteada uma pergunta')
    time.sleep(1)
    print('- Responda-a digitando o número correspondente à opção')
    time.sleep(1.2)
    print('- A cada acerto você ganha uma moeda')
    time.sleep(1)
    print('- A cada 3 acertos consecutivos você escolhe a categoria\n  para ganhar uma estrela')
    time.sleep(2)
    print('- Você ganha o jogo se conseguir todas as 6 estrelas!\n')
    time.sleep(3)
    powerups()
    
def shop():
    a=''
    print('1 - 10000$ = 5£')
    print('2 - 50000$ = 10£')
    print('3 - 100000$ = 50£')
    print('4 - 1000000$ = 100£')
    print('5 - Sair\n')
    while a!='5':
        a=input()
        if a=='1':
            if gw[player]>=5:
                md[player]+=10000
                gw[player]-=5
        if a=='2':
            if gw[player]>=10:
                md[player]+=50000
                gw[player]-=10
        if a=='3':
            if gw[player]>=50:
                md[player]+=100000
                gw[player]-=50
        if a=='4':
            if gw[player]>=100:
                md[player]+=1000000
                gw[player]-=100
        if a=='5':break

def making():
    qc='0'
    print('Escolha uma categoria:\n')
    print('1 - Tecnologia')
    print('2 - Cinema')
    print('3 - Literatura')
    print('4 - Música')
    print('5 - História')
    print('6 - Ciências\n')
    while qc not in '123456':
        qc=input()
    qc=int(qc)
    print('\n\n\nEscreva sua pergunta:')
    qu=input()
    print('\n\n\nEscreva a opção correta')
    qr=input()
    print('\n\n\nEscreva outras 3 opções erradas')
    q1=input()
    q2=input()
    q3=input()
    print('\n\n\nEscreva uma dica para a pergunta')
    qh=input()
    print('\n\n\nSua pergunta ficou assim:\n')
    print(qu+'\n\n'+qr+'\n'+q1+'\n'+q2+'\n'+q3+'\n\nDica: '+qh)
    print('\nAperte Enter para confirmar ou\nDigite algo para refazer')
    ba=input()
    if ba!='':making()
    else:
        if qc==1:file='Tecnologia.txt'
        if qc==2:file='Cinema.txt'
        if qc==3:file='Literatura.txt'
        if qc==4:file='Música.txt'
        if qc==5:file='História.txt'
        if qc==6:file='Ciências.txt'
        fileopen=open(folder+file,'a')
        fileopen.write('-\n')
        fileopen.write('?'+qu+'\n')
        fileopen.write('>'+qr+'\n')
        fileopen.write('X'+q1+'\n')
        fileopen.write('X'+q2+'\n')
        fileopen.write('X'+q3+'\n')
        fileopen.write('!'+qh+'\n')
        fileopen.close()
        
        if qst[9][0]==0:
            qst[9][0]=100
            print('\nPARABÉNS!\n\n'+qst[9][1]+'\n+400$')
            for t in range(0,players):md[t]+=400
            time.sleep(5)

def conquistas():
    for i in qst:
        print(str(i[0])+'%  - '+i[1])
    print('\n\n\n\n')

def rank():
    ind=0
    print('-PLACAR-')
    for i in range(0, len(sc)):
        ind+=1
        print(str(ind)+'° '+nm[i]+' - '+str(sc[i]))
    print()

def powerups():
    print('Você pode gastar suas moedas com esses itens:')
    print('(x) elimina 1 opção = 10$')
    print('(xx) elimina 2 opções = 30$')
    print('(+) dá uma segunda chance = 20$')
    print('(=) pula para a próxima pergunta = 50$')
    print('(!) mostra uma dica = 10$')
    print('(@) sorteia outra pergunta = '+str(sp[player]*2)+'$')
    print('(÷) adiciona mais tempo = 20$\n')
    print('para usá-los digite o que se encontra em parênteses\nmas apenas funcionará se tiver moedas!\nDigite P para mostrar todos os power-ups')
    time.sleep(5)

def gameover():
    print('\nFIM DE JOGO\n')
    time.sleep(2)
    print('perguntas: '+str(i))
    print('acertos: '+str(ac))
    print('erros: '+str(er)+'\n')
    if mode==1:
        bonus=(ac*5)+sc[player]
        md[player]+=bonus
    print('PONTUAÇÃO: '+str(sc[player]))
    if mode==1:print('+'+str(bonus)+'$\n')
    
    if qst[18][0]<100:
        if int(er)==0:
            qst[18][0]=100
            print('\nPARABÉNS!\n\n'+qst[1][1]+'\n+1000$')
            for t in range(0,players):md[t]+=1000
            time.sleep(5)

if datetime.datetime.now().hour-pastime>=3:
    fh+=1
    pastime=datetime.datetime.now().hour

#MENU PRINCIPAL
print('--TRIVIA--')
print('por KaiXtr\n')
while mode not in '123':
    time.sleep(3)
    print('1>Arcade')
    print('2>Contrarrelógio')
    print('3>Infinito')
    print('4>Criar')
    print('5>Loja')
    print('6>Placar')
    print('7>Conquistas')
    print('8>Ajuda\n')
    while mode not in '12345678':
        mode=input()
    if mode=='4':making()
    elif mode=='5':shop()
    elif mode=='6':rank()
    elif mode=='7':conquistas()
    elif mode=='8':instructions()
    else:
        if fh==0:
            print('\nVocê não tem fichas...=(\n')
            mode='0'
    if mode not in '123':mode='0'
    
mode=int(mode)
print('\nQuantos vão jogar?')
players=int(input())
sp=[]
fh-=1
for t in range(0,players):
    bar.append(0)
    cc.append(0)
    sp.append(1)
print('\n\n\n\n\n\n\n\n\n\n\n\n')

#JOGO
while True:
    ind=0
    pp=100
    
    #CATEGORIA
    if players>1:print(nm[player]+', Sua Vez')
    if bar[player]==3:
        c=0
        print('Escolha uma Categoria\n')
        for ix in '123456':
            if ix in ctg:
                c+=1
                if ix=='1':print(str(c)+' - Tecnologia')
                if ix=='2':print(str(c)+' - Cinema')
                if ix=='3':print(str(c)+' - Literatura')
                if ix=='4':print(str(c)+' - Música')
                if ix=='5':print(str(c)+' - História')
                if ix=='6':print(str(c)+' - Ciências')
        while c not in ctg:
            c=input()
        c=int(c)-1
        ix=0
    elif bar[player]<3:
        while yn.startswith('@'):
            c=int(random.randint(0,5))
            if mode!=1:yn='n'
            if mode==1:
                print('Sorteando Pergunta...\n')
                time.sleep(3)
                if c==0:print('TECNOLOGIA')
                if c==1:print('CINEMA')
                if c==2:print('LITERATURA')
                if c==3:print('MÚSICA')
                if c==4:print('HISTÓRIA')
                if c==5:print('CIÊNCIAS')
                if md[player]>=2:
                    yn=input()
                    if yn=='@':
                        sp[player]*=2
                        md[player]-=sp[player]
                        pp-=20
                else:yn='n'
        yn='n'
        print()
    if c==0:lis=qgk
    if c==1:lis=qcm
    if c==2:lis=qlt
    if c==3:lis=qmc
    if c==4:lis=qhs
    if c==5:lis=qcc
    
    #PERGUNTAS E RESPOSTAS
    r=int(random.randint(0,len(lis)-1))
    print(str(i)+') '+lis[r][0]+'\n')
    time.sleep(1)
    op=int(random.randint(0,4))
    if op==0:op='1234'
    if op==1:op='3142'
    if op==2:op='2431'
    if op==3:op='4213'
    if op==4:op='2143'
    for t in op:
        ix+=1
        print(str(ix)+' - '+(lis[r][int(t)])[1:])
        if t=='1':ans=ix
        time.sleep(0.2)
    print()
    
    #POWERUPS
    a=input()
    if a=='P':
        powerups()
        a=input()
    if a=='x' and md[player]>=100:
        print()
        print((lis[r][1])[1:])
        yy=random.randint(2,4)
        print((lis[r][yy])[1:])
        xx=yy
        while xx==yy:
            xx=random.randint(2,4)
        print((lis[r][xx])[1:])
        md[player]-=100
        pp-=10
        print()
        a=input()
    elif a=='xx' and md[player]>=300:
        print()
        print((lis[r][1])[1:])
        yy=random.randint(2,4)
        print((lis[r][yy])[1:])
        md[player]-=300
        pp-=30
        print()
        a=input()
    elif a=='+' and md[player]>=200:
        a=input()
        pp-=20
        if int(a)!=ans:
            print('SEGUNDA CHANCE\n')
            md[player]-=200
            a=input()
    elif a=='!' and md[player]>=100:
        md[player]-=10
        pp-=100
        print(lis[r][5])
        a=input()
    elif a=='=' and md[player]>=500:
        pp=0
        md[player]-=500
        a=ans
        print(a)
    elif a=='÷' and md[player]>=200:
        pp-=40
        md[player]-=200
        tempo+=20
        a=input
    print()
    
    #RESULTADOS
    if a==str(ans):
        if mode!=1:md[player]+=10
        if qst[8][0]<100:qst[8][0]=0
        if qst[0][0]<100:
            qst[0][0]+=10
            if qst[0][0]==100:
                print('\nPARABÉNS!\n\n'+qst[0][1]+'\n+100$')
                for t in range(0,players):md[t]+=100
                time.sleep(5)
        if qst[1][0]<100:
            qst[1][0]+=2
            if qst[1][0]==100:
                print('\nPARABÉNS!\n\n'+qst[1][1]+'\n+200$')
                for t in range(0,players):md[t]+=500
                time.sleep(5)
        for ind in '234567':
            ind=int(ind)
            if qst[ind][0]<100:
                if c==ind-2:qst[ind][0]+=5
                if qst[ind][0]==100:
                    print('\nPARABÉNS!\n\n'+qst[ind][1]+'\n+300$')
                    for t in range(0,players):md[t]+=300
                    time.sleep(5)
        if mode==1:
            if bar[player]<3:
                bar[player]+=1
            elif bar[player]==3:
                if cc[player]<6:
                    cc[player]+=1
                    bar[player]=0
                if cc[player]==6:
                    gameover()
                    break
                del(ctg[c])
        print('Resposta Certa!')
        ac+=1
    else:
        if a!='@':
            print('Resposta Errada...')
            er+=1
            if qst[8][0]<100:
                qst[8][0]+=20
                if qst[8][0]==100:
                    print('\nPARABÉNS!\n\n'+qst[8][1]+'\n+200$')
                    for t in range(0,players):md[t]+=200
                    time.sleep(5)
            bar[player]=0
            pp/=10
            if mode==3:
                gameover()
                break
    sc[player]+=pp
    if bar[player]==0:print('')
    if bar[player]==1:print('-')
    if bar[player]==2:print('--')
    if bar[player]==3:print('---')
    print(str(md[player])+'$')
    print(str(cc[player])+'*')
    i+=1
    ix=0
    yn='@'
    player+=1
    if player==players:player=0
    if mode==1:time.sleep(3)
    else:time.sleep(1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n')

#SALVAMENTO
fileopen=open(folder+'UserData.db','w')
for i in range(0,len(nm)):
    fileopen.write(nm[i]+'\n')
    fileopen.write(str(sc[i])+'\n')
    fileopen.write(str(md[i])+'\n')
    fileopen.write(str(gw[i])+'\n')
fileopen.write('H'+str(pastime)+'\nEND\n')
fileopen.close()

fileopen=open(folder+'Trophies.db','w')
for i in qst:
    if i[0]<10:qqn='00'+str(i[0])
    elif i[0]<100:qqn='0'+str(i[0])
    else:qqn=str(i[0])
    fileopen.write(qqn+i[1]+'\n')
fileopen.close()