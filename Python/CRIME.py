import colorama
import random
import time
import os

def telefone():
	lugares=['Itália','Grécia','Espanha','Portugal','França','Alemanha','Inglaterra','Suécia']
	caso=[' uma pessoa caiu da janela do quinto andar, dizem que é um suicídio, mas uma pessoa foi avistada na janela, sua missão é descobrir quem a derrubou e prendê-la',' uma pessoa foi assassinada na praça do relógio, descubra quem é o assassino',' um objeto raro foi roubado do museu nacional, descubra quem é o ladrão', ' o presidente foi sequestrado no palácio da alvorada, encontre-o e prenda o sequestrador']
	opt=0
	
	while int(opt)!=1:
		c=round(random.randint(0,len(caso)-1))
		print('Há um caso para você, '+name+','+caso[c])
		print('\nAceita esse caso?\n1 - Sim\n2 - Não\n')
		opt=input('>')
	os.system('clear')

print(colorama.Fore.GREEN)
print('XXX  XXXX  X  X   X  XXX')
print('X    X  X     X X X  X')
print('X    XX    X  X X X  XX')
print('X    X  X  X  X   X  X')
print('XXX  X  X  X  X   X  XXX')
print(colorama.Style.RESET_ALL)
time.sleep(1)
print('Você é...\n\n1 - Menino\n2 - Menina\n')
gen=0
while gen not in ['1','2']:
	gen=input('>')
gen=int(gen)
print('\nQual é o seu nome?')
name=input('>')
if gen==1:name='Sr. '+name
if gen==2:name='Sra. '+name

os.system('clear')
print('\nVocê está no ESCRITÓRIO\nO telefone está tocando\n')
time.sleep(1)
print('1 - Telefone')
print('2 - Computador')
print('3 - Máquina de Escrever')
print('4 - Video-Cassete')
print('5 - Documentos')
print('6 - Apontador')
print('7 - Sair\n')
act=input('>')
if int(act)==1:telefone()

while act!=6:
	print('Você está na CENA DO CRIME\n')
	print('1 - Corpo')
	print('2 - Policial')
	print('3 - Testemunha')
	print('4 - Testemunha')
	print('5 - Chão')
	print('6 - Sair\n')
	act=input('>')
	act=int(act)
	print()
	
	if act==1:print('Há um buraco nas costas dele, mas não há nenhuma bala...\n')
	elif act==2:print('O corpo caiu para frente, provavelmente foi derrubado ou acertado por algo, mas o buraco nas costas é algo a se questionar\n')
	elif act==3:print('Eu estava presente no momento em que a vítima foi morta, eu vi uma pessoa chegar por trás e tampar sua boca, não consegui escutar muito pois um barulho alto de broca começou a aparecer, ele estava usando óculos\n')
	elif act==4:print('Estava pela praça momentos antes do assassinato, o sujeito tinha bigode fino e usava colete amarelo, acho que era um construtor')
	elif act==5:print('Há muito sangue no chão...eww! Distraído, o assassino deixou algumas pegadas no chão, elas apontam para o cais')
	time.sleep(1)
	print()