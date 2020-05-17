from tkinter import *
from random import *

#Variables
poss=[1,2,3,4,5,6,7,8,9]
score_1=0
score_2=0
color=1
mode=0
mark="X"
active=False
t=1
l=1
lan="English"
x=[]
o=[]


#Functions
def gmode(m):
	global mode
	global active
	mode=m
	lb["text"]="Reset"
	m1.grid_forget()
	m2.grid_forget()
	s1.grid(row=4, column=1)
	s2.grid(row=4, column=3)
	active=True

def button(b):
	global active
	if active==True:
		if b==1 and b1["text"]=="":
			b1["text"]=mark
		if b==2 and b2["text"]=="":
			b2["text"]=mark
		if b==3 and b3["text"]=="":
			b3["text"]=mark
		if b==4 and b4["text"]=="":
			b4["text"]=mark
		if b==5 and b5["text"]=="":
			b5["text"]=mark
		if b==6 and b6["text"]=="":
			b6["text"]=mark
		if b==7 and b7["text"]=="":
			b7["text"]=mark
		if b==8 and b8["text"]=="":
			b8["text"]=mark
		if b==9 and b9["text"]=="":
			b9["text"]=mark
		if (b not in x) and (b not in o):
			npc(b)

def npc(b):
	global score_1
	global score_2
	global mode
	global mark
	global active
	global x
	global o

	#Add to List
	if mark=="X":
		x.append(b)
	if mark=="O":
		o.append(b)

	#Check X
	if 1 in x:
		if 2 in x:
			if 3 in x:
				win(1)
				b1["bg"]="blue"
				b2["bg"]="blue"
				b3["bg"]="blue"

		if 4 in x:
			if 7 in x:
				win(1)
				b1["bg"]="blue"
				b4["bg"]="blue"
				b7["bg"]="blue"
		if 5 in x:
			if 9 in x:
				win(1)
				b1["bg"]="blue"
				b5["bg"]="blue"
				b9["bg"]="blue"

	if 2 in x:
		if 5 in x:
			if 8 in x:
				win(1)
				b2["bg"]="blue"
				b5["bg"]="blue"
				b8["bg"]="blue"

	if 3 in x:
		if 6 in x:
			if 9 in x:
				win(1)
				b3["bg"]="blue"
				b6["bg"]="blue"
				b9["bg"]="blue"
		if 5 in x:
			if 7 in x:
				win(1)
				b3["bg"]="blue"
				b5["bg"]="blue"
				b7["bg"]="blue"

	if 4 in x:
		if 5 in x:
			if 6 in x:
				win(1)
				b4["bg"]="blue"
				b5["bg"]="blue"
				b6["bg"]="blue"

	if 7 in x:
		if 8 in x:
			if 9 in x:
				win(1)
				b7["bg"]="blue"
				b8["bg"]="blue"
				b9["bg"]="blue"

	#NPC Random
	poss.remove(b)
	if mode==1:
		if active==True:
			if len(poss)>0:
				i=(round(randint(1,len(poss))))-1
				p=poss[i]
				poss.remove(poss[i])
				o.append(p)

				if p==1:
					b1["text"]="O"
				if p==2:
					b2["text"]="O"
				if p==3:
					b3["text"]="O"
				if p==4:
					b4["text"]="O"
				if p==5:
					b5["text"]="O"
				if p==6:
					b6["text"]="O"
				if p==7:
					b7["text"]="O"
				if p==8:
					b8["text"]="O"
				if p==9:
					b9["text"]="O"
			else:
				if active==True:
					lb["text"]="Draw"
					active=False

	#Check O
	if 1 in o:
		if 2 in o:
			if 3 in o:
				win(2)
				b1["bg"]="red"
				b2["bg"]="red"
				b3["bg"]="red"
		if 4 in o:
			if 7 in o:
				win(2)
				b1["bg"]="red"
				b4["bg"]="red"
				b7["bg"]="red"
		if 5 in o:
			if 9 in o:
				win(2)
				b1["bg"]="red"
				b5["bg"]="red"
				b9["bg"]="red"

	if 2 in o:
		if 5 in o:
			if 8 in o:
				win(2)
				b2["bg"]="red"
				b5["bg"]="red"
				b8["bg"]="red"

	if 3 in o:
		if 6 in o:
			if 9 in o:
				win(2)
				b3["bg"]="red"
				b6["bg"]="red"
				b9["bg"]="red"
		if 5 in o:
			if 7 in o:
				win(2)
				b3["bg"]="red"
				b5["bg"]="red"
				b7["bg"]="red"

	if 7 in o:
		if 8 in o:
			if 9 in o:
				win(2)
				b7["bg"]="red"
				b8["bg"]="red"
				b9["bg"]="red"

	#Change Mark
	if mode==2:
		if mark=="X":
			mark=False
		if mark=="O":
			mark=True

		mark=not mark

		if mark==False:
			mark="X"
		if mark==True:
			mark="O"

def win(p):
	global score_1
	global score_2
	global mode
	global active

	if p==1:
		score_1+=1
		s1["text"]=score_1
		if mode==1:
			if lan=="English":
				lb["text"]="You Win!"
			if lan=="Português":
				lb["text"]="Você Venceu!"
			if lan=="Español":
				lb["text"]="Tú Ganas!"
			if lan=="Français":
				lb["text"]="Tu Gagnes"

		if mode==2:
			if lan=="English":
				lb["text"]="1P Wins"
			if lan=="Português":
				lb["text"]="1P Venceu"
			if lan=="Español":
				lb["text"]="1P Gana"
			if lan=="Français":
				lb["text"]="1P Gagné"
	if p==2:
		score_2+=1
		s2["text"]=score_2
		if mode==1:
			if lan=="English":
				lb["text"]="You Lose..."
			if lan=="Português":
				lb["text"]="Você Perdeu..."
			if lan=="Español":
				lb["text"]="Tú Pierdes..."
			if lan=="Français":
				lb["text"]="Tu Perds..."
		if mode==2:
			if lan=="English":
				lb["text"]="2P Wins"
			if lan=="Português":
				lb["text"]="2P Venceu"
			if lan=="Español":
				lb["text"]="2P Gana"
			if lan=="Français":
				lb["text"]="2P Gagné"

	active=False

def again():
	global active
	global score_1
	global score_2
	global poss
	global theme
	global x
	global o

	if mode>0:
		b1["text"]=""
		b2["text"]=""
		b3["text"]=""
		b4["text"]=""
		b5["text"]=""
		b6["text"]=""
		b7["text"]=""
		b8["text"]=""
		b9["text"]=""
		colors(color)
		poss=[1,2,3,4,5,6,7,8,9]

		if x==[]:
			s1["text"]=0
			s2["text"]=0
			score_1=0
			score_2=0
		if lan=="English":
			lb["text"]="Reset"
		if lan=="Português" or lan=="Español":
			lb["text"]="Reiniciar"
		if lan=="Français":
			lb["text"]="Redémarrer"

		x=[]
		o=[]
		active=True

def colors(th):
	global color

	if th==1:
		root["bg"]="orange"
		bts["bg"]="orange"
		oth["bg"]="orange"
		b1["bg"]="gray"
		b2["bg"]="gray"
		b3["bg"]="gray"
		b4["bg"]="gray"
		b5["bg"]="gray"
		b6["bg"]="gray"
		b7["bg"]="gray"
		b8["bg"]="gray"
		b9["bg"]="gray"
		b1["activebackground"]="darkgray"
		b2["activebackground"]="darkgray"
		b3["activebackground"]="darkgray"
		b4["activebackground"]="darkgray"
		b5["activebackground"]="darkgray"
		b6["activebackground"]="darkgray"
		b7["activebackground"]="darkgray"
		b8["activebackground"]="darkgray"
		b9["activebackground"]="darkgray"
	if th==2:
		root["bg"]="white"
		bts["bg"]="white"
		oth["bg"]="white"
		b1["bg"]="snow"
		b2["bg"]="snow"
		b3["bg"]="snow"
		b4["bg"]="snow"
		b5["bg"]="snow"
		b6["bg"]="snow"
		b7["bg"]="snow"
		b8["bg"]="snow"
		b9["bg"]="snow"
		b1["activebackground"]="gray"
		b2["activebackground"]="gray"
		b3["activebackground"]="gray"
		b4["activebackground"]="gray"
		b5["activebackground"]="gray"
		b6["activebackground"]="gray"
		b7["activebackground"]="gray"
		b8["activebackground"]="gray"
		b9["activebackground"]="gray"
	if th==3:
		root["bg"]="black"
		bts["bg"]="black"
		oth["bg"]="black"
		b1["bg"]="gray"
		b2["bg"]="gray"
		b3["bg"]="gray"
		b4["bg"]="gray"
		b5["bg"]="gray"
		b6["bg"]="gray"
		b7["bg"]="gray"
		b8["bg"]="gray"
		b9["bg"]="gray"
		b1["activebackground"]="darkgray"
		b2["activebackground"]="darkgray"
		b3["activebackground"]="darkgray"
		b4["activebackground"]="darkgray"
		b5["activebackground"]="darkgray"
		b6["activebackground"]="darkgray"
		b7["activebackground"]="darkgray"
		b8["activebackground"]="darkgray"
		b9["activebackground"]="darkgray"
	if th==4:
		root["bg"]="black"
		bts["bg"]="black"
		oth["bg"]="black"
		b1["bg"]="green"
		b2["bg"]="green"
		b3["bg"]="green"
		b4["bg"]="green"
		b5["bg"]="green"
		b6["bg"]="green"
		b7["bg"]="green"
		b8["bg"]="green"
		b9["bg"]="green"
		b1["activebackground"]="darkgreen"
		b2["activebackground"]="darkgreen"
		b3["activebackground"]="darkgreen"
		b4["activebackground"]="darkgreen"
		b5["activebackground"]="darkgreen"
		b6["activebackground"]="darkgreen"
		b7["activebackground"]="darkgreen"
		b8["activebackground"]="darkgreen"
		b9["activebackground"]="darkgreen"
	if th==5:
		root["bg"]="black"
		bts["bg"]="black"
		oth["bg"]="black"
		b1["bg"]="aqua"
		b2["bg"]="aqua"
		b3["bg"]="aqua"
		b4["bg"]="aqua"
		b5["bg"]="aqua"
		b6["bg"]="aqua"
		b7["bg"]="aqua"
		b8["bg"]="aqua"
		b9["bg"]="aqua"
		b1["activebackground"]="darkcyan"
		b2["activebackground"]="darkcyan"
		b3["activebackground"]="darkcyan"
		b4["activebackground"]="darkcyan"
		b5["activebackground"]="darkcyan"
		b6["activebackground"]="darkcyan"
		b7["activebackground"]="darkcyan"
		b8["activebackground"]="darkcyan"
		b9["activebackground"]="darkcyan"
	if th==6:
		root["bg"]="white"
		bts["bg"]="white"
		oth["bg"]="white"
		b1["bg"]="red"
		b2["bg"]="orange"
		b3["bg"]="yellow"
		b4["bg"]="greenyellow"
		b5["bg"]="green"
		b6["bg"]="cyan"
		b7["bg"]="blue"
		b8["bg"]="violet"
		b9["bg"]="pink"
		b1["activebackground"]="darkred"
		b2["activebackground"]="darkorange"
		b3["activebackground"]="gold"
		b4["activebackground"]="green"
		b5["activebackground"]="darkgreen"
		b6["activebackground"]="darkcyan"
		b7["activebackground"]="darkblue"
		b8["activebackground"]="darkviolet"
		b9["activebackground"]="magenta"
	if th==7:
		root["bg"]="black"
		bts["bg"]="black"
		oth["bg"]="black"
		b1["bg"]="red"
		b2["bg"]="orange"
		b3["bg"]="yellow"
		b4["bg"]="greenyellow"
		b5["bg"]="green"
		b6["bg"]="cyan"
		b7["bg"]="blue"
		b8["bg"]="violet"
		b9["bg"]="pink"
		b1["activebackground"]="darkred"
		b2["activebackground"]="darkorange"
		b3["activebackground"]="gold"
		b4["activebackground"]="green"
		b5["activebackground"]="darkgreen"
		b6["activebackground"]="darkcyan"
		b7["activebackground"]="darkblue"
		b8["activebackground"]="darkviolet"
		b9["activebackground"]="magenta"

	color=th

def lang(lg):
	global lan

	if lg==1:
		root.title("Tic Tac Toe")

		if lan=="Português":
			bar.entryconfigure('Jogo', label='Game')
			theme.entryconfigure('Padrão', label='Default')
			game.entryconfigure('Tema', label='Theme')
			game.entryconfigure('Idioma', label='Language')
			theme.entryconfigure('Claro', label='Light')
			theme.entryconfigure('Escuro', label='Dark')
			theme.entryconfigure('Colorido', label='Rainbow')
			theme.entryconfigure('Escuro e Colorido', label='Dark Rainbow')

		if lan=="Español":
			bar.entryconfigure('Juego', label='Game')
			theme.entryconfigure('Defecto', label='Default')
			game.entryconfigure('Tema', label='Theme')
			game.entryconfigure('Idioma', label='Language')
			theme.entryconfigure('Ligero', label='Light')
			theme.entryconfigure('Oscuro', label='Dark')
			theme.entryconfigure('Vistoso', label='Rainbow')
			theme.entryconfigure('Oscuro y Vistoso', label='Dark Rainbow')

		if lan=="Français":
			bar.entryconfigure('Jeu', label='Game')
			theme.entryconfigure('Défaut', label='Default')
			game.entryconfigure('Thème', label='Theme')
			game.entryconfigure('Langue', label='Language')
			theme.entryconfigure('Lumière', label='Light')
			theme.entryconfigure('Foncé', label='Dark')
			theme.entryconfigure('Coloré', label='Rainbow')
			theme.entryconfigure('Coloré Foncé', label='Dark Rainbow')

		lan="English"
	if lg==2:
		root.title("Jogo da Velha")

		if lan=="English":
			bar.entryconfigure('Game', label='Jogo')
			theme.entryconfigure('Default', label='Padrão')
			game.entryconfigure('Theme', label='Tema')
			game.entryconfigure('Language', label='Idioma')
			theme.entryconfigure('Light', label='Claro')
			theme.entryconfigure('Dark', label='Escuro')
			theme.entryconfigure('Rainbow', label='Colorido')
			theme.entryconfigure('Dark Rainbow', label='Escuro e Colorido')

		if lan=="Español":
			bar.entryconfigure('Juego', label='Jogo')
			theme.entryconfigure('Defecto', label='Padrão')
			theme.entryconfigure('Ligero', label='Claro')
			theme.entryconfigure('Oscuro', label='Escuro')
			theme.entryconfigure('Vistoso', label='Colorido')
			theme.entryconfigure('Oscuro y Vistoso', label='Escuro e Colorido')

		if lan=="Français":
			bar.entryconfigure('Jeu', label='Jogo')
			theme.entryconfigure('Défaut', label='Padrão')
			game.entryconfigure('Thème', label='Tema')
			game.entryconfigure('Langue', label='Idioma')
			theme.entryconfigure('Lumière', label='Claro')
			theme.entryconfigure('Foncé', label='Escuro')
			theme.entryconfigure('Coloré', label='Colorido')
			theme.entryconfigure('Coloré Foncé', label='Escuro e Colorido')

		lan="Português"
	if lg==3:
		root.title("Tres en Línea")

		if lan=="English":
			bar.entryconfigure('Game', label='Juego')
			theme.entryconfigure('Default', label='Defecto')
			game.entryconfigure('Theme', label='Tema')
			game.entryconfigure('Language', label='Idioma')
			theme.entryconfigure('Light', label='Ligero')
			theme.entryconfigure('Dark', label='Oscuro')
			theme.entryconfigure('Rainbow', label='Vistoso')
			theme.entryconfigure('Dark Rainbow', label='Oscuro y Vistoso')

		if lan=="Português":
			bar.entryconfigure('Jogo', label='Juego')
			theme.entryconfigure('Padrão', label='Defecto')
			theme.entryconfigure('Claro', label='Ligero')
			theme.entryconfigure('Escuro', label='Oscuro')
			theme.entryconfigure('Colorido', label='Vistoso')
			theme.entryconfigure('Escuro e Colorido', label='Oscuro y Vistoso')

		if lan=="Français":
			bar.entryconfigure('Jeu', label='Juego')
			theme.entryconfigure('Défaut', label='Defecto')
			game.entryconfigure('Thème', label='Tema')
			game.entryconfigure('Langue', label='Idioma')
			theme.entryconfigure('Lumière', label='Ligero')
			theme.entryconfigure('Foncé', label='Oscuro')
			theme.entryconfigure('Coloré', label='Vistoso')
			theme.entryconfigure('Coloré Foncé', label='Oscuro y Vistoso')

		lan="Español"
	if lg==4:
		root.title("Tic-Tac-Toe")

		if lan=="English":
			bar.entryconfigure('Game', label='Jeu')
			theme.entryconfigure('Default', label='Défaut')
			game.entryconfigure('Theme', label='Thème')
			game.entryconfigure('Language', label='Langue')
			theme.entryconfigure('Light', label='Lumière')
			theme.entryconfigure('Dark', label='Foncé')
			theme.entryconfigure('Rainbow', label='Coloré')
			theme.entryconfigure('Dark Rainbow', label='Coloré Foncé')

		if lan=="Português":
			bar.entryconfigure('Jogo', label='Jeu')
			theme.entryconfigure('Padrão', label='Défaut')
			game.entryconfigure('Tema', label='Thème')
			game.entryconfigure('Idioma', label='Langue')
			theme.entryconfigure('Claro', label='Lumière')
			theme.entryconfigure('Escuro', label='Foncé')
			theme.entryconfigure('Colorido', label='Coloré')
			theme.entryconfigure('Escuro e Colorido', label='Coloré Foncé')

		if lan=="Español":
			bar.entryconfigure('Juego', label='Jeu')
			theme.entryconfigure('Defecto', label='Défaut')
			game.entryconfigure('Tema', label='Thème')
			game.entryconfigure('Idioma', label='Langue')
			theme.entryconfigure('Ligero', label='Lumière')
			theme.entryconfigure('Oscuro', label='Foncé')
			theme.entryconfigure('Vistoso', label='Coloré')
			theme.entryconfigure('Oscuro y Vistoso', label='Coloré Foncé')

		lan="Français"

#Window
root=Tk()
root.title("Tic Tac Toe")
root.geometry("200x200+500+300")
root.iconbitmap(default='Tic.ico')
root.resizable(0,0)
root.attributes("-toolwindow")

#Menus
bar=Menu(root)
root.config(menu=bar)
game=Menu(bar, tearoff=0)
theme=Menu(game, tearoff=0)
language=Menu(game, tearoff=0)
bar.add_cascade(label="Game", menu=game)
game.add_cascade(label="Theme", menu=theme)
game.add_cascade(label="Language", menu=language)
theme.add_radiobutton(label="Default", command=lambda:colors(1), variable=t, value=1)
theme.add_radiobutton(label="Light", command=lambda:colors(2), variable=t, value=2)
theme.add_radiobutton(label="Dark", command=lambda:colors(3), variable=t, value=3)
theme.add_radiobutton(label="Hacker", command=lambda:colors(4), variable=t, value=4)
theme.add_radiobutton(label="Tron", command=lambda:colors(5), variable=t, value=5)
theme.add_radiobutton(label="Rainbow", command=lambda:colors(6), variable=t, value=6)
theme.add_radiobutton(label="Dark Rainbow", command=lambda:colors(7), variable=t, value=7)

language.add_radiobutton(label="English", command=lambda:lang(1), variable=l, value=1)
language.add_radiobutton(label="Português", command=lambda:lang(2), variable=l, value=2)
language.add_radiobutton(label="Español", command=lambda:lang(3), variable=l, value=3)
language.add_radiobutton(label="Français", command=lambda:lang(4), variable=l, value=4)

#Widgets
bts=Frame(root, padx=50, pady=20)
b1=Button(bts, width=3, height=2, command=lambda:button(1))
b2=Button(bts, width=3, height=2, command=lambda:button(2))
b3=Button(bts, width=3, height=2, command=lambda:button(3))
b4=Button(bts, width=3, height=2, command=lambda:button(4))
b5=Button(bts, width=3, height=2, command=lambda:button(5))
b6=Button(bts, width=3, height=2, command=lambda:button(6))
b7=Button(bts, width=3, height=2, command=lambda:button(7))
b8=Button(bts, width=3, height=2, command=lambda:button(8))
b9=Button(bts, width=3, height=2, command=lambda:button(9))
oth=Frame(root)
m1=Button(oth, text="1P", command=lambda:gmode(1))
m2=Button(oth, text="2P", command=lambda:gmode(2))
s1=Label(oth, text=score_1, width=4, relief='ridge')
s2=Label(oth, text=score_2, width=4, relief='ridge')
lb=Button(oth, text="Play", command=again)

#Position
bts.grid(row=1, column=1)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)
oth.grid(row=2, column=1)
m1.grid(row=4, column=1)
lb.grid(row=4, column=2)
m2.grid(row=4, column=3)

colors(1)
root.mainloop()