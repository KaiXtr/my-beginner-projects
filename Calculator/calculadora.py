from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math
import re

hexde=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
hislb=[0]
hislh=['']

n1=0
op=""
n2=0
nm=0
dtm="decimal"
res=0
dt="decimal"
par=0
resv=[0,0,0,0]
opv=['','','','']
yey=False
lan="English"
indic=0


#FUNÇÕES
def text(e):
	if e.char!='':
		if e.char in '1234567890':
			lb["text"]=e.char
		if e.char in '+-/*':
			operation(e.char)
		if e.char in '.,':
			dot()
		if e.char=='=':
			result()
		if e.char=='c':
			c()

def historic(h):
	global indic
	global hislb
	global hislh
	global res
	global op
	global n2

	if h==1:
		if indic<(len(hislb)-1):
			indic+=1
			if re.search(r'.',hislb[indic]):
				res=float(hislb[indic])
			else:
				res=int(hislb[indic])
	if h==2:
		if indic>0:
			indic-=1
			if re.search(r'.',hislb[indic]):
				res=float(hislb[indic])
			else:
				res=int(hislb[indic])
	if h==3:
		if indic==(len(hislb)-1):
			hislb.append(str(res))
			hislh.append(lh["text"])
			indic+=1
		else:
			indic+=1
			hislb[indic]=str(res)
			hislh[indic]=lh["text"]
			hislb=hislb[:indic+1]
			hislh=hislh[:indic+1]

	lb["text"]=hislb[indic]
	lh["text"]=hislh[indic]

def number(n):
	global res
	global par

	if lb["text"]==str(res) or lb["text"]==str(nm) or lb["text"]==str(resv[par-1]):
		lb["text"]=str(n)
	else:
		lb["text"]+=str(n)

	print(str(n1)+"-"+str(n2)+"-"+str(res))

def operation(o,s=False):
	global dt
	global op
	global n1
	global n2
	global res
	global yey
	global indic

	if lb["text"]!="0" or o=="x" or o=="÷":
		if n1==0:
			if dt=="decimal":
				n1=int(lb["text"])
			elif dt=="float":
				n1=float(lb["text"])

			lh["text"]+=str(n1)+" "+o+" "

		else:
			if dt=="decimal":
				n2=int(lb["text"])
			elif dt=="float":
				n2=float(lb["text"])

			lh["text"]+=str(n2)
			if s==False:
				lh["text"]+=" "+o+" "

	elif lb["text"]=="0":
		if o=="+" or o=="-":
			lb["text"]=o

	if n1!=0 and n2!=0:
		yey=False

	if o!="%":
		if o!="+":
			if o!="-":
				lb["text"]="0"

	if n2!=0 and yey==False and o!="%":
		if op=='+':
			if res==0:
				res=n1+n2
			else:
				res=n2+res
		elif op=='-':
			if res==0:
				res=n1-n2
			else:
				res=res-n2
		elif op=='*':
			if res==0:
				res=n1*n2
			else:
				res=n2*res
		elif op=='/':
			if res==0:
				res=n1/n2
			else:
				res=n2/res
			dt="float"
		elif op=='R':
			if res==0:
				res=n1%n2
			else:
				res=n2%res

	if lb["text"]!="+":
		if lb["text"]!="-":
			lb["text"]=str(res)
			historic(3)

	if o=="√":
		res=math.sqrt(n1)
		lb["text"]=str(res)
		n1=res
		dt="float"
	elif o=="²":
		res=n1**2
		lb["text"]=str(res)
		n1=res
	elif o=="%":
		n2=int(lb["text"])
		pr=n1*(n2/100)
		dt="float"
		if op=='+':
			res=n1+pr
			lb["text"]=str(res)
		if op=='-':
			res=n1-pr
			lb["text"]=str(res)

	if o!='%':
		op=str(o)
	print(dt)
	print(str(n1) + "-" + str(n2) + "-" + str(res))

def parenteses(p):
	global n1
	global n2
	global op
	global res
	global dt
	global par
	global resv
	global opv

	if p==1:
		if par<3:
			if res!=0:
				resv[par]=int(res)
			else:
				resv[par]=int(n1)
			lb["text"]=str(resv[par])
			res=0
			n1=0
			n2=0
			opv[par]=op
			op=""

		if par==2:
			lh["text"]+="{ "
		elif par==1:
			lh["text"]+="[ "
		elif par==0:
			lh["text"]+="( "

		if par<3:
			par+=1
	if p==2:
		if par>0:
			operation(op,True)
			if opv[par]=="+":
				res=resv[par-1]+res
			elif opv[par]=="-":
				res=resv[par-1]-res
			elif opv[par]=="x":
				res=resv[par-1]*res
			elif opv[par]=="÷":
				res=resv[par-1]/res
			lb["text"]=res

		if par==1:
			lh["text"]+=" )"
		elif par==2:
			lh["text"]+=" ]"
		elif par==3:
			lh["text"]+=" }"

		if par>0:
			par-=1

def commum(c):
	global n1
	global n2
	x=1
	y=2
	n1c=[]
	n2c=[]

	if n1!=0 and n2!=0:
		if c==1:
			text=str(lh["text"])
			lh["text"]="wait..."
			i=0
			r=10
			s=False
			while r<100000 and s==False:
				a=False
				while len(n1c)<r:
					i+=1
					n1c.append(n1*i)

				i=0
				while len(n2c)<r:
					i+=1
					n2c.append(n2*i)

				i=0
				while x!=y and a==False:
					x=n1c[i]
					i+=1
					t=0
					while (t<(len(n2c)-1)) and (y!=x):
						y=n2c[t]
						t+=1

					if (t==len(n2c)-1) and (y!=x) and (i==(len(n1c))):
						r+=10
						a=True

					if y==x:
						s=True
						lh["text"]=text

					if i==len(n1c) and r==100000:
						lh["text"]="can't find mmc..."
						s=True


			lb["text"]=str(x)
		if c==2:
			text=str(lh["text"])
			lh["text"]="wait..."
			i=0
			r=10
			s=False
			while r<100000 and s==False:
				a=False
				while len(n1c)<r:
					i+=1
					n1c.append(n1/i)
					print(n1c)

				i=0
				while len(n2c)<r:
					i+=1
					n2c.append(n2/i)
					print(n2c)

				i=r
				while x!=y and a==False:
					x=n1c[i]
					i-=1
					print(str(x)+'X')
					t=r
					while (t<(len(n2c)-1)) and (y!=x):
						y=n2c[t]
						t-=1
						print(str(y)+'Y')

					if (t==0) and (y!=x) and (i==(len(n1c))):
						r+=10
						print('OUTRA VEZ...')
						a=True

					if y==x:
						s=True
						print('ENCONTRADO')
						lh["text"]=text

					if i==0 and r==100000:
						lh["text"]="can't find mmc..."
						s=True


			lb["text"]=str(x)

def arredondar(a):
	if a==1:
		lb["text"]=str(math.ceil(res))
	if a==2:
		lb["text"]=str(math.floor(res))

def memory(o):
	global n1
	global n2
	global nm
	global dtm
	global dt
	global res

	if o=="save":
		if lb["text"]!="0":
			nm=lb["text"]
			dtm=dt
	if o=="call":
		lb["text"]=str(nm)
		dt=dtm
	if o=="clear":
		nm=0
		lb["text"]="0"
	if o=="add":
		n2=lb["text"]
		if dtm=="decimal":
			if dt=="decimal":
				res=int(nm)+int(n2)
			elif dt=="float":
				res=int(nm)+float(n2)
		elif dtm=="float":
			if dt=="decimal":
				res=float(nm)+int(n2)
			elif dt=="float":
				res=float(nm)+float(n2)
		lb["text"]=str(res)
	if o=="subtract":
		n2=lb["text"]
		if dtm=="decimal":
			if dt=="decimal":
				res=int(n2)-int(nm)
			elif dt=="float":
				res=int(n2)-float(nm)
		elif dtm=="float":
			if dt=="decimal":
				res=float(n2)-int(nm)
			elif dt=="float":
				res=float(n2)-float(nm)
		lb["text"]=str(res)

def c():
	global op
	global dt
	global res
	global n1
	global n2
	global yey
	global par
	global resv

	op=""
	dt="decimal"
	res=0
	n1=0
	n2=0
	yey=False
	lh["text"]=""
	lb["text"]="0"
	par=0
	resv=[0,0,0,0]
	print(dt)

def ce():
	lb["text"]="0"

def dot():
	global dt
	if dt!="float":
		lb["text"]+="."
		dt="float"

def delta():
	a=re.search(r"X²",lb["text"],re.I)
	b=re.search(r"X",lb["text"],re.I)
	return((b*b)(-4*(a*c)))

def baskara():
	d=delta()
	r1=(-b+(math.sqrt(d)))/(2*a)
	r2=(-b-(math.sqrt(d)))/(2*a)

def pitagoras():
	c1=0
	c2=0
	return math.sqrt((c1**c1)+(c2**c2))

def numbtype(t):
	global dt
	new=0
	nu=int(lb["text"])

	if t==1:
		dt="binary"
		lb["text"]=bin(int(lb["text"]))
	if t==2:
		dt="decimal"
		lb["text"]=int(lb["text"])
	if t==3:
		new+=2
		lb["text"]=str(new)
		dt="octal"
	if t==4:
		while nu>=16:
			new+=1
			nu-=16

		lb["text"]=str(new)+hexde[nu]
		dt="hexadecimal"

	print(dt)

def result(e=None):
	global n1
	global n2
	global op
	global dt
	global res
	global yey
	global indic

	if n2==0:
		if dt=="decimal":
			n2=int(lb["text"])
		elif dt=="float":
			n2=float(lb["text"])
	else:
		if dt=="decimal":
			n2=int(lb["text"])
			n1=int(res)
		elif dt=="float":
			n2=float(lb["text"])
			n1=float(res)

	if op=='+':
		res=n1+n2
	elif op=='-':
		res=n1-n2
	elif op=='x':
		res=n1*n2
	elif op=='÷':
		res=n1/n2
		dt="float"
	elif op=='R':
		res=n1%n2

	if dt=="hexadecimal":
		while res>16:
			res-=10
			n1+=16
		res=hexde[res]+n1

	lb["text"]=str(res)
	lh["text"]+=str(n2)+" ="
	historic(3)
	lh["text"]=""
	#n1=res
	n1=0
	n2=0
	yey=True
	print(dt)
	print(str(n1) + "-" + str(n2) + "-" + str(res))

def color(t):
	global b
	global n
	global o
	global m
	global na
	global oa
	global ma
	global col

	if t==1:
		b='#F2F2F2'

		n='#F2F2F2'
		o='#CCCCCC'
		m='#AAAAAA'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'
	if t==2:
		b='#FFB200'

		n='#F2F2F2'
		o='#CCCCCC'
		m='#AAAAAA'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'
	if t==3:
		b='#000000'

		n='#919191'
		o='#CCCCCC'
		m='#AAAAAA'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'
	if t==4:
		b='#000000'

		n='#009933'
		o='#007C29'
		m='#005B1E'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'
	if t==5:
		b='#DDF9FF'

		n='#B5E3FF'
		o='#97C7E5'
		m='#72A9CC'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'
	if t==6:
		b='#FFD3F8'

		n='#FCBAF2'
		o='#EA9DDE'
		m='#D87FCB'

		na='#FFFFFF'
		oa='#DBDBDB'
		ma='#B7B7B7'

	janela["bg"] = b

	bt0['bg'] = n
	bt1['bg'] = n
	bt2['bg'] = n
	bt3['bg'] = n
	bt4['bg'] = n
	bt5['bg'] = n
	bt6['bg'] = n
	bt7['bg'] = n
	bt8['bg'] = n
	bt9['bg'] = n
	btp['bg'] = n
	btr['bg'] = n

	if col==True:
		bta['bg'] = o
		bts['bg'] = o
		btm['bg'] = o
		btd['bg'] = o
		btrq['bg'] = o
		btpr['bg'] = o
		btrs['bg'] = o
		btpc['bg'] = o
		btce['bg'] = o
		btc['bg'] = o

		btpe['bg'] = o
		btpd['bg'] = o
		btmmc['bg'] = o
		btmdc['bg'] = o
		btau['bg'] = o
		btad['bg'] = o

		btmc['bg'] = m
		btms['bg'] = m
		btmr['bg'] = m
		btma['bg'] = m
		btmm['bg'] = m

		hup['bg'] = m
		hdw['bg'] = m
	if col==False:
		bta['bg'] = n
		bts['bg'] = n
		btm['bg'] = n
		btd['bg'] = n
		btrq['bg'] = n
		btpr['bg'] = n
		btrs['bg'] = n
		btpc['bg'] = n
		btce['bg'] = n
		btc['bg'] = n

		btpe['bg'] = n
		btpd['bg'] = n
		btmmc['bg'] = n
		btmdc['bg'] = n
		btau['bg'] = n
		btad['bg'] = n

		btmc['bg'] = n
		btms['bg'] = n
		btmr['bg'] = n
		btma['bg'] = n
		btmm['bg'] = n

		hup['bg'] = n
		hdw['bg'] = n

	bt0['activebackground'] = na
	bt1['activebackground'] = na
	bt2['activebackground'] = na
	bt3['activebackground'] = na
	bt4['activebackground'] = na
	bt5['activebackground'] = na
	bt6['activebackground'] = na
	bt7['activebackground'] = na
	bt8['activebackground'] = na
	bt9['activebackground'] = na
	btr['activebackground'] = na
	btp['activebackground'] = na

	if col==True:
		bta['activebackground'] = oa
		bts['activebackground'] = oa
		btm['activebackground'] = oa
		btd['activebackground'] = oa
		btrq['activebackground'] = oa
		btpr['activebackground'] = oa
		btrs['activebackground'] = oa
		btpc['activebackground'] = oa
		btce['activebackground'] = oa
		btc['activebackground'] = oa

		btpe['activebackground'] = oa
		btpd['activebackground'] = oa
		btmmc['activebackground'] = oa
		btmdc['activebackground'] = oa
		btau['activebackground'] = oa
		btad['activebackground'] = oa

		btmc['activebackground'] = ma
		btms['activebackground'] = ma
		btmr['activebackground'] = ma
		btma['activebackground'] = ma
		btmm['activebackground'] = ma

		hup['activebackground'] = ma
		hdw['activebackground'] = ma
	if col==False:
		bta['activebackground'] = na
		bts['activebackground'] = na
		btm['activebackground'] = na
		btd['activebackground'] = na
		btrq['activebackground'] = na
		btpr['activebackground'] = na
		btrs['activebackground'] = na
		btpc['activebackground'] = na
		btce['activebackground'] = na
		btc['activebackground'] = na

		btpe['activebackground'] = na
		btpd['activebackground'] = na
		btmmc['activebackground'] = na
		btmdc['activebackground'] = na
		btau['activebackground'] = na
		btad['activebackground'] = na

		btmc['activebackground'] = na
		btms['activebackground'] = na
		btmr['activebackground'] = na
		btma['activebackground'] = na
		btmm['activebackground'] = na

		hup['activebackground'] = ma
		hdw['activebackground'] = ma

	savecolors()

def colbot(sw=True):
	global col
	global n
	global o
	global m

	if sw==True:
		col=not col

	if col==False:
		bta["bg"] = n
		bts["bg"] = n
		btm["bg"] = n
		btd["bg"] = n
		btrq["bg"] = n
		btpc["bg"] = n
		btpr["bg"] = n
		btrs["bg"] = n
		btce["bg"] = n
		btc["bg"] = n
		btmc["bg"] = n
		btmr["bg"] = n
		btms["bg"] = n
		btma["bg"] = n
		btmm["bg"] = n
	if col==True:
		bta["bg"] = o
		bts["bg"] = o
		btm["bg"] = o
		btd["bg"] = o
		btrq["bg"] = o
		btpc["bg"] = o
		btpr["bg"] = o
		btrs["bg"] = o
		btce["bg"] = o
		btc["bg"] = o
		btmc["bg"] = m
		btmr["bg"] = m
		btms["bg"] = m
		btma["bg"] = m
		btmm["bg"] = m

	if sw==True:
		savedata()

def memoshow(sw=True):
	global mem
	global mor
	global adv

	if sw==True:
		mem=not mem

	if mem==True:
		print("y")
		if mor==True:
			janela.geometry("255x363+500+300")
		if mor==False:
			janela.geometry("207x363+500+300")

		if adv==True:
			btpe.grid(row=0, column=0)
		if mor==True:
			btmm.grid(row=0, column=5)
		btmc.grid(row=0, column=1)
		btmr.grid(row=0, column=2)
		btms.grid(row=0, column=3)
		btma.grid(row=0, column=4)

	if mem==False:
		if mor==True:
			janela.geometry("255x313+500+300")
		if mor==False:
			janela.geometry("207x313+500+300")

		if adv==True:
			btpe.grid_forget()
		if mor==True:
			btmm.grid_forget()
		btmc.grid_forget()
		btmr.grid_forget()
		btms.grid_forget()
		btma.grid_forget()

	if sw==True:
		savedata()

def moreshow(sw=True):
	global mor
	if sw==True:
		mor=not mor

	if mor==True:
		if mem==True:
			janela.geometry("255x363+500+300")
		if mem==False:
			janela.geometry("255x313+500+300")
		lh["width"]=34
		lb["width"]=22

		if mem==True:
			btmm.grid(row=0, column=5)
		btrq.grid(row=1, column=5)
		btpr.grid(row=2, column=5)
		btrs.grid(row=3, column=5)
		btpc.grid(row=4, column=5)
		btce.grid(row=5, column=5)

	if mor==False:
		if mem==False:
			janela.geometry("207x313+500+300")
		if mem==True:
			janela.geometry("207x363+500+300")
		lh["width"]=27
		lb["width"]=17

		if mem==True:
			btmm.grid_forget()
		btrq.grid_forget()
		btpr.grid_forget()
		btrs.grid_forget()
		btpc.grid_forget()
		btce.grid_forget()

	if sw==True:
		savedata()

def advashow(sw=True):
	global adv
	global mem
	if sw==True:
		adv=not adv

	if adv==True:
		if mem==True:
			janela.geometry("255x363+500+300")
		if mem==False:
			janela.geometry("255x313+500+300")
		lh["width"]=34
		lb["width"]=22

		if mem==True:
			btpe.grid(row=0, column=0)
		btpd.grid(row=1, column=0)
		btmmc.grid(row=2, column=0)
		btmdc.grid(row=3, column=0)
		btau.grid(row=4, column=0)
		btad.grid(row=5, column=0)

	if adv==False:
		if mem==True:
			janela.geometry("207x363+500+300")
		if mem==False:
			janela.geometry("207x313+500+300")
		lh["width"]=27
		lb["width"]=17

		if mem==True:
			btpe.grid_forget()
		btpd.grid_forget()
		btmmc.grid_forget()
		btmdc.grid_forget()
		btau.grid_forget()
		btad.grid_forget()

	if sw==True:
		savedata()

def histshow(sw=True):
	global his
	if sw==True:
		his=not his

	if his==True:
		hup.grid(row=1, column=0)
		hdw.grid(row=2, column=0)
	if his==False:
		hup.grid_forget()
		hdw.grid_forget()

	if sw==True:
		savedata()

def invenumb(sw=True):
	global mem
	global inv

	if sw==True:
		inv=not inv

	if inv==True:
		bt1.grid(row=3, column=1)
		bt2.grid(row=3, column=2)
		bt3.grid(row=3, column=3)
		bt4.grid(row=2, column=1)
		bt5.grid(row=2, column=2)
		bt6.grid(row=2, column=3)
		bt7.grid(row=1, column=1)
		bt8.grid(row=1, column=2)
		bt9.grid(row=1, column=3)

	if inv==False:
		bt1.grid(row=1, column=1)
		bt2.grid(row=1, column=2)
		bt3.grid(row=1, column=3)
		bt4.grid(row=2, column=1)
		bt5.grid(row=2, column=2)
		bt6.grid(row=2, column=3)
		bt7.grid(row=3, column=1)
		bt8.grid(row=3, column=2)
		bt9.grid(row=3, column=3)

	if sw==True:
		savedata()

def lang(l,i=True):
	global lan

	if l=="English":
		if lan!="English":
			janela.title("Calculator")
			view.entryconfigure('Tema', label='Theme')
			view.entryconfigure('Idioma', label='Language')
			theme.entryconfigure('Azul', label='Blue')
			theme.entryconfigure('Rosa', label='Pink')
			help.entryconfigure('Sobre...', label='About...')

			if lan=="Português":
				bar.entryconfigure('Exibir', label='View')
				bar.entryconfigure('Ajuda', label='Help')
				view.entryconfigure('Botões', label='Buttons')
				theme.entryconfigure('Antigo', label='Old')
				theme.entryconfigure('Padrão', label='Default')
				theme.entryconfigure('Escuro', label='Dark')
				buttons.entryconfigure('Botões de Memória', label='Memory Buttons')
				buttons.entryconfigure('Botões Adicionais', label='Additional Buttons')
				buttons.entryconfigure('Botões Avançados', label='Advanced Buttons')
				buttons.entryconfigure('Botões de Histórico', label='History Buttons')
				buttons.entryconfigure('Inverter Números', label='Invert Numbers')
				buttons.entryconfigure('Botões Coloridos', label='Colored Buttons')

			if lan=="Español":
				bar.entryconfigure('Vista', label='View')
				bar.entryconfigure('Ayuda', label='Help')
				view.entryconfigure('Botones', label='Buttons')
				theme.entryconfigure('Antiguo', label='Old')
				theme.entryconfigure('Estandár', label='Default')
				theme.entryconfigure('Oscuro', label='Dark')
				buttons.entryconfigure('Botones de Memoria', label='Memory Buttons')
				buttons.entryconfigure('Botones Adicionales', label='Additional Buttons')
				buttons.entryconfigure('Botones Avanzados', label='Advanced Buttons')
				buttons.entryconfigure('Botones de Historial', label='History Buttons')
				buttons.entryconfigure('Invertir Números', label='Invert Numbers')
				buttons.entryconfigure('Botones de Colorados', label='Colored Buttons')

			lan = "English"
	if l=="Português":
		if lan!="Português":
			janela.title("Calculadora")

			if lan=="English":
				bar.entryconfigure('View', label='Exibir')
				bar.entryconfigure('Help', label='Ajuda')
				view.entryconfigure('Theme',label='Tema')
				view.entryconfigure('Language', label='Idioma')
				view.entryconfigure('Buttons', label='Botões')
				theme.entryconfigure('Old', label='Antigo')
				theme.entryconfigure('Default', label='Padrão')
				theme.entryconfigure('Dark', label='Escuro')
				theme.entryconfigure('Blue', label='Azul')
				theme.entryconfigure('Pink', label='Rosa')
				buttons.entryconfigure('Memory Buttons', label='Botões de Memória')
				buttons.entryconfigure('Additional Buttons', label='Botões Adicionais')
				buttons.entryconfigure('Advanced Buttons', label='Botões Avançados')
				buttons.entryconfigure('History Buttons', label='Botões de Histórico')
				buttons.entryconfigure('Invert Numbers', label='Inverter Números')
				buttons.entryconfigure('Colored Buttons', label='Botões Coloridos')
				help.entryconfigure('About...', label='Sobre...')

			if lan=="Español":
				bar.entryconfigure('Vista', label='Exibir')
				bar.entryconfigure('Ayuda', label='Ajuda')
				view.entryconfigure('Botones', label='Botões')
				theme.entryconfigure('Antiguo', label='Antigo')
				theme.entryconfigure('Estandár', label='Padrão')
				theme.entryconfigure('Oscuro', label='Escuro')
				buttons.entryconfigure('Botones de Memoria', label='Botões de Memória')
				buttons.entryconfigure('Botones Adicionales', label='Botões Adicionais')
				buttons.entryconfigure('Botones Avanzados', label='Botões Avançados')
				buttons.entryconfigure('Botones de Historial', label='Botões de Histórico')
				buttons.entryconfigure('Invertir Números', label='Inverter Números')
				buttons.entryconfigure('Botones de Colorados', label='Botões Coloridos')

			lan="Português"
	if l=="Español":
		if lan!="Español":
			janela.title("Calculadora")

			if lan=="English":
				bar.entryconfigure('View', label='Vista')
				bar.entryconfigure('Help', label='Ayuda')
				view.entryconfigure('Theme',label='Tema')
				view.entryconfigure('Language', label='Idioma')
				view.entryconfigure('Buttons', label='Botones')
				theme.entryconfigure('Old', label='Antiguo')
				theme.entryconfigure('Default', label='Estandár')
				theme.entryconfigure('Dark', label='Oscuro')
				theme.entryconfigure('Blue', label='Azul')
				theme.entryconfigure('Pink', label='Rosa')
				buttons.entryconfigure('Memory Buttons', label='Botones de Memoria')
				buttons.entryconfigure('Additional Buttons', label='Botones Adicionales')
				buttons.entryconfigure('Advanced Buttons', label='Botones Avanzados')
				buttons.entryconfigure('History Buttons', label='Botones de Historial')
				buttons.entryconfigure('Invert Numbers', label='Invertir Números')
				buttons.entryconfigure('Colored Buttons', label='Botones de Colorados')
				help.entryconfigure('About...', label='Sobre...')

			if lan=="Português":
				bar.entryconfigure('Exibir', label='Vista')
				bar.entryconfigure('Ajuda', label='Ayuda')
				view.entryconfigure('Botões', label='Botones')
				theme.entryconfigure('Antigo', label='Antiguo')
				theme.entryconfigure('Padrão', label='Estandár')
				theme.entryconfigure('Escuro', label='Oscuro')
				buttons.entryconfigure('Botões de Memória', label='Botones de Memoria')
				buttons.entryconfigure('Botões Adicionais', label='Botones Adicionales')
				buttons.entryconfigure('Botões Avançados', label='Botones Avanzados')
				buttons.entryconfigure('Botões de Histórico', label='Botones de Historial')
				buttons.entryconfigure('Inverter Números', label='Invertir Números')
				buttons.entryconfigure('Botões Coloridos', label='Botones de Colorados')

			lan="Español"

	if i==True:
		savedata()

def abo():
	if lan=="English":
		messagebox.showinfo("About", " Program by KaiXtr \n Made in PyCharm CE \n Tkinter Graphic Module \n 24/11/2017")
	elif lan=="Português":
		messagebox.showinfo("Sobre", " Programa por KaiXtr \n Criado no PyCharm CE \n Tkinter Graphic Module \n 24/11/2017")
	elif lan=="Español":
		messagebox.showinfo("Sobre", " Programa por KaiXtr \n Hecho in PyCharm CE \n Tkinter Graphic Module \n 24/11/2017")

def savecolors():
	for i in b,n,o,m,na,oa,ma:
		if i.endswith('\n')==True:
			i=i[0:-1]
	file=open("CalculatorColors.db",'w')
	file.write(b+"\n"+n+"\n"+o+"\n"+m+"\n"+na+"\n"+oa+"\n"+ma+"\n")
	file.close()

def savedata():
	global col
	global mem
	global mor
	global adv
	global inv
	global lan

	for i in str(col),str(mem),str(mor),str(adv),str(inv),str(his),lan:
		if i.endswith('\n')==True:
			i=i[0:-1]
			print(i)

	file=open("CalculatorData.db", 'w')
	file.write(str(col)+"\n"+str(mem)+"\n"+str(mor)+"\n"+str(adv)+"\n"+str(inv)+"\n"+str(his)+"\n"+lan)
	file.close()

def invert():
	global col
	global mem
	global mor
	global adv
	global inv
	global his

	print(str(col) + str(mem) + str(mor) + str(adv) + str(inv) + str(his))
	col = not col
	mem = not mem
	mor = not mor
	adv = not adv
	inv = not inv
	his = not his
	print(str(col) + str(mem) + str(mor) + str(adv) + str(inv) + str(his))

#DADOS SALVOS
file=open('CalculatorColors.db','r')

b=file.readline()[0:-1]
n=file.readline()[0:-1]
o=file.readline()[0:-1]
m=file.readline()[0:-1]

na=file.readline()[0:-1]
oa=file.readline()[0:-1]
ma=file.readline()[0:-1]

file.close()


#JANELA
janela=Tk()
janela.title("Calculator")
janela.geometry("280x330+500+300")
#janela.resizable(0,0)
#janela.iconbitmap(default='PI.ico')
janela["bg"]=b

#MENUS
bar=Menu(janela)
janela.config(menu=bar)

active=BooleanVar()
active.set(True)
t=2
ln=1

#View
view=Menu(bar, tearoff=0)
bar.add_cascade(label='View', menu=view)
theme=Menu(view, tearoff=0)
language=Menu(view, tearoff=0)
buttons=Menu(view, tearoff=0)
view.add_cascade(label='Theme', menu=theme)
view.add_cascade(label='Language', menu=language)
view.add_cascade(label='Buttons', menu=buttons)
view.add_separator()
view.add_radiobutton(label='Binary', command=lambda:numbtype(1))
view.add_radiobutton(label='Decimal', command=lambda:numbtype(2))
view.add_radiobutton(label='Octonal', command=lambda:numbtype(3))
view.add_radiobutton(label='Hexadecimal', command=lambda:numbtype(4))

#View-Theme
theme.add_radiobutton(label='Old', command=lambda:color(1), variable=t, value=1)
theme.add_radiobutton(label='Default', command=lambda:color(2), variable=t, value=2)
theme.add_radiobutton(label='Dark', command=lambda:color(3), variable=t, value=3)
theme.add_radiobutton(label='Hacker', command=lambda:color(4), variable=t, value=4)
theme.add_radiobutton(label='Blue', command=lambda:color(5), variable=t, value=5)
theme.add_radiobutton(label='Pink', command=lambda:color(6), variable=t, value=6)

#View-Language
language.add_radiobutton(label="English", command=lambda:lang("English"), variable=ln, value=1)
language.add_radiobutton(label="Português", command=lambda:lang("Português"), variable=ln, value=2)
language.add_radiobutton(label="Español", command=lambda:lang("Español"), variable=ln, value=3)

#View-Buttons
buttons.add_checkbutton(label='Memory Buttons', command=memoshow)
buttons.add_checkbutton(label='Additional Buttons', command=moreshow)
buttons.add_checkbutton(label='Advanced Buttons', command=advashow)
buttons.add_checkbutton(label='History Buttons', command=histshow)
buttons.add_checkbutton(label='Invert Numbers', command=invenumb)
buttons.add_checkbutton(label='Colored Buttons', onvalue=1, offvalue=False, variable=active, command=colbot)

#Help
help=Menu(bar, tearoff=0)
bar.add_cascade(label='Help', menu=help)
help.add_command(label='About...', command=abo)

#LABELS
f_labels=Frame(janela, bg='white')
lh=Label(f_labels, width=27, height=1, text="", bg='white')
lb=Label(f_labels, width=17, height=0, text="0", bg='white', font='arial 15')

#HISTORIC
hup=Button(f_labels, text="^", width=2, height=1, bg=m, activebackground=ma, command=lambda:historic(1))
hdw=Button(f_labels, text="v", width=2, height=1, bg=m, activebackground=ma, command=lambda:historic(2))

f_num=Frame(janela)

#MEMORY BUTTONS
btmc=Button(f_num, text="MC", width=5, height=2, bg=m, activebackground=ma, command=lambda:memory('clear'))
btms=Button(f_num, text="MS", width=5, height=2, bg=m, activebackground=ma, command=lambda:memory('save'))
btmr=Button(f_num, text="MR", width=5, height=2, bg=m, activebackground=ma, command=lambda:memory('call'))
btma=Button(f_num, text="M+", width=5, height=2, bg=m, activebackground=ma, command=lambda:memory('add'))
btmm=Button(f_num, text="M-", width=5, height=2, bg=m, activebackground=ma, command=lambda:memory('subtract'))

#NÚMEROS
bt1=Button(f_num, text="1", width=5, height=2, bg=n, activebackground=na, command=lambda:number(1))
bt2=Button(f_num, text="2", width=5, height=2, bg=n, activebackground=na, command=lambda:number(2))
bt3=Button(f_num, text="3", width=5, height=2, bg=n, activebackground=na, command=lambda:number(3))
bt4=Button(f_num, text="4", width=5, height=2, bg=n, activebackground=na, command=lambda:number(4))
bt5=Button(f_num, text="5", width=5, height=2, bg=n, activebackground=na, command=lambda:number(5))
bt6=Button(f_num, text="6", width=5, height=2, bg=n, activebackground=na, command=lambda:number(6))
bt7=Button(f_num, text="7", width=5, height=2, bg=n, activebackground=na, command=lambda:number(7))
bt8=Button(f_num, text="8", width=5, height=2, bg=n, activebackground=na, command=lambda:number(8))
bt9=Button(f_num, text="9", width=5, height=2, bg=n, activebackground=na, command=lambda:number(9))
bt0=Button(f_num, text="0", width=5, height=2, bg=n, activebackground=na, command=lambda:number(0))

#PONTO
# img=PhotoImage(file='Button.png')
btp=Button(f_num, text=".", width=5, height=2 ,command=dot, bg=n, activebackground=na)

#OPERAÇÕES BÁSICAS
bta=Button(f_num, text="+", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation("+"))
bts=Button(f_num, text="-", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation("-"))
btm=Button(f_num, text="x", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation("*"))
btd=Button(f_num, text="÷", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation("/"))

#OPERAÇÕES MÉDIAS
btrq=Button(f_num, text="√", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation('√'))
btpr=Button(f_num, text="%", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation('%'))
btrs=Button(f_num, text="R", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation('R'))
btpc=Button(f_num, text="X²", width=5, height=2, bg=o, activebackground=oa, command=lambda:operation('²'))

#OPERAÇÕES AVANÇADAS
btpe=Button(f_num, text="(", width=5, height=2, bg=o, activebackground=oa, command=lambda:parenteses(1))
btpd=Button(f_num, text=")", width=5, height=2, bg=o, activebackground=oa, command=lambda:parenteses(2))
btmmc=Button(f_num, text="MMC", width=5, height=2, bg=o, activebackground=oa, command=lambda:commum(1))
btmdc=Button(f_num, text="MMD", width=5, height=2, bg=o, activebackground=oa, command=lambda:commum(2))
btau=Button(f_num, text="^", width=5, height=2, bg=o, activebackground=oa, command=lambda:arredondar(1))
btad=Button(f_num, text="v", width=5, height=2, bg=o, activebackground=oa, command=lambda:arredondar(2))

btdlt=Button(f_num, text="∆", width=5, height=2, bg=o, activebackground=oa, command=lambda:delta())
btbsk=Button(f_num, text="b∆", width=5, height=2, bg=o, activebackground=oa, command=lambda:baskara())
btptg=Button(f_num, text="h2", width=5, height=2, bg=o, activebackground=oa, command=lambda:pitagoras())

#TEXTO
#btr=Button(f_num, text="=", width=19, height=2 ,command=result, bg=n, activebackground=na)
btr=Button(f_num, text="=", width=5, height=2 ,command=result, bg=n, activebackground=na)
btc=Button(f_num, text="C", width=5, height=2, command=c, bg=o, activebackground=oa)
btce=Button(f_num, text="CE", width=5, height=2, command=ce, bg=o, activebackground=oa)


#POSIÇÃO
f_labels.grid(row=1, column=1)
lh.grid(row=1, column=1)
lb.grid(row=2, column=1)

hup.grid(row=1, column=0)
hdw.grid(row=2, column=0)

f_num.grid(row=2, column=1)
bt1.grid(row=1, column=1)
bt2.grid(row=1, column=2)
bt3.grid(row=1, column=3)
bt4.grid(row=2, column=1)
bt5.grid(row=2, column=2)
bt6.grid(row=2, column=3)
bt7.grid(row=3, column=1)
bt8.grid(row=3, column=2)
bt9.grid(row=3, column=3)
bt0.grid(row=4, column=1, columnspan=2, sticky=W+E)

btp.grid(row=4, column=3)

bta.grid(row=1, column=4)
bts.grid(row=2, column=4)
btm.grid(row=3, column=4)
btd.grid(row=4, column=4)

btr.grid(row=5, column=1, columnspan=3, sticky=W+E)
btc.grid(row=5, column=4)


#DADOS SALVOS
file=open('CalculatorData.db','r')

col=file.readline()
mem=file.readline()
mor=file.readline()
adv=file.readline()
inv=file.readline()
his=file.readline()

l=file.readline()
lang(l,False)

file.close()


#CARREGAR DADOS
if col=="True": col=True
if col=="False": col=False
if mem=="True": mem=True
if mem=="False": mem=False
if mor=="True": mor=True
if mor=="False": mor=False
if adv=="True": adv=True
if adv=="False": adv=False
if inv=="True": inv=True
if inv=="False": inv=False
if his=="True": his=True
if his=="False": his=False

print("C"+col)
print("M"+mem)
print("O"+mor)
print("A"+adv)
print("I"+inv)
print("H"+his)
colbot(sw=False)
memoshow(sw=False)
moreshow(sw=False)
invenumb(sw=False)
advashow(sw=False)
histshow(sw=False)

janela.bind('<Key>', text)
janela.bind('<Return>', result)
janela.mainloop()