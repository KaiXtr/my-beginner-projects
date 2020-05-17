from tkinter import *

word=""
revealed=[]
i=0

def play():
	global word
	global revealed

	word=ew.get()
	if word!="":
		ew.grid_forget()
		pl.grid_forget()
		lw.grid(row=1, column=1)
		#while i<len(word):
		#	revealed.append("_")
		lw["text"]=revealed

def letter(l):
	if lw["text"]!="":
		for i in len(word):
			if l in word:
				revealed[i]=l
		lw["text"]=revealed


root=Tk()
root.title('Jogo da Forca')
root.geometry("400x300+500+500")
root.resizable(0,0)

st=Frame(root)
ew=Entry(st)
pl=Button(st, text='Play', command=lambda:play())
lw=Label(st)

bts=Frame(root)
ba=Button(bts, text='A', command=lambda:letter('a'))
bb=Button(bts, text='B', command=lambda:letter('b'))
bc=Button(bts, text='C', command=lambda:letter('c'))
bd=Button(bts, text='D', command=lambda:letter('d'))
be=Button(bts, text='E', command=lambda:letter('e'))
bf=Button(bts, text='F', command=lambda:letter('f'))
bg=Button(bts, text='G', command=lambda:letter('g'))
bh=Button(bts, text='H', command=lambda:letter('h'))
bi=Button(bts, text='I', command=lambda:letter('i'))
bj=Button(bts, text='J', command=lambda:letter('j'))
bk=Button(bts, text='K', command=lambda:letter('k'))
bl=Button(bts, text='L', command=lambda:letter('l'))
bm=Button(bts, text='M', command=lambda:letter('m'))
bn=Button(bts, text='N', command=lambda:letter('n'))
bo=Button(bts, text='O', command=lambda:letter('o'))
bp=Button(bts, text='P', command=lambda:letter('p'))
bq=Button(bts, text='Q', command=lambda:letter('q'))
br=Button(bts, text='R', command=lambda:letter('r'))
bs=Button(bts, text='S', command=lambda:letter('s'))
bt=Button(bts, text='T', command=lambda:letter('t'))
bu=Button(bts, text='U', command=lambda:letter('u'))
bv=Button(bts, text='V', command=lambda:letter('v'))
bw=Button(bts, text='W', command=lambda:letter('w'))
bx=Button(bts, text='X', command=lambda:letter('x'))
by=Button(bts, text='Y', command=lambda:letter('y'))
bz=Button(bts, text='Z', command=lambda:letter('z'))

st.grid(row=1, column=1)
ew.grid(row=1, column=1)
pl.grid(row=1, column=2)
bts.grid(row=2, column=1)
ba.grid(row=1, column=1)
bb.grid(row=1, column=2)
bc.grid(row=1, column=3)
bd.grid(row=1, column=4)
be.grid(row=1, column=5)
bf.grid(row=1, column=6)
bg.grid(row=1, column=7)
bh.grid(row=1, column=8)
bi.grid(row=1, column=9)
bj.grid(row=1, column=10)
bk.grid(row=1, column=11)
bl.grid(row=1, column=12)
bm.grid(row=1, column=13)
bn.grid(row=2, column=1)
bo.grid(row=2, column=2)
bp.grid(row=2, column=3)
bq.grid(row=2, column=4)
br.grid(row=2, column=5)
bs.grid(row=2, column=6)
bt.grid(row=2, column=7)
bu.grid(row=2, column=8)
bv.grid(row=2, column=9)
bw.grid(row=2, column=10)
bx.grid(row=2, column=11)
by.grid(row=2, column=12)
bz.grid(row=2, column=13)

root.mainloop()