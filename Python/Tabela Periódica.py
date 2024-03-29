from tkinter import *
from tkinter.font import Font

def element(e):
	pass

root=Tk()
root.title('Tabela Periódica')
root.geometry('400x300+400+400')
root['bg']='green'
root.resizable(0,0)

font=Font(family='Consolas', size='10', weight='bold')
gn='blue'
am='red'
sm='yellow'
m='green'

he=Button(root, text='He', bg=gn, font=font, command=lambda:element(2))
ne=Button(root, text='Ne', bg=gn, font=font, command=lambda:element(10))
ar=Button(root, text='Ar', bg=gn, font=font, command=lambda:element(18))
kr=Button(root, text='Kr', bg=gn, font=font, command=lambda:element(36))
xe=Button(root, text='Xe', bg=gn, font=font, command=lambda:element(54))
rn=Button(root, text='Rn', bg=gn, font=font, command=lambda:element(86))
uuo=Button(root, text='Uuo', bg=gn, font=font, command=lambda:element(118))

h=Button(root, text='H', bg=am, font=font, command=lambda:element(1))
c=Button(root, text='C', bg=am, font=font, command=lambda:element(6))
n=Button(root, text='N', bg=am, font=font, command=lambda:element(7))
o=Button(root, text='O', bg=am, font=font, command=lambda:element(8))
f=Button(root, text='F', bg=am, font=font, command=lambda:element(9))
p=Button(root, text='P', bg=am, font=font, command=lambda:element(15))
s=Button(root, text='S', bg=am, font=font, command=lambda:element(16))
cl=Button(root, text='Cl', bg=am, font=font, command=lambda:element(17))
se=Button(root, text='Se', bg=am, font=font, command=lambda:element(34))
br=Button(root, text='Br', bg=am, font=font, command=lambda:element(35))
i=Button(root, text='I', bg=am, font=font, command=lambda:element(53))
at=Button(root, text='At', bg=am, font=font, command=lambda:element(85))

b=Button(root, text='B', bg=sm, font=font, command=lambda:element(5))
ai=Button(root, text='Ai', bg=sm, font=font, command=lambda:element(13))
si=Button(root, text='Si', bg=sm, font=font, command=lambda:element(14))
ga=Button(root, text='Ga', bg=sm, font=font, command=lambda:element(31))
ge=Button(root, text='Ge', bg=sm, font=font, command=lambda:element(32))
_as=Button(root, text='As', bg=sm, font=font, command=lambda:element(33))
_in=Button(root, text='In', bg=sm, font=font, command=lambda:element(49))
sn=Button(root, text='Sn', bg=sm, font=font, command=lambda:element(50))
sb=Button(root, text='Sb', bg=sm, font=font, command=lambda:element(51))
te=Button(root, text='Te', bg=sm, font=font, command=lambda:element(52))
ti=Button(root, text='Ti', bg=sm, font=font, command=lambda:element(81))
pb=Button(root, text='Pb', bg=sm, font=font, command=lambda:element(82))
bi=Button(root, text='Bi', bg=sm, font=font, command=lambda:element(83))
po=Button(root, text='Po', bg=sm, font=font, command=lambda:element(84))
uut=Button(root, text='Uut', bg=sm, font=font, command=lambda:element(113))
uuq=Button(root, text='Uuq', bg=sm, font=font, command=lambda:element(114))
uup=Button(root, text='Uup', bg=sm, font=font, command=lambda:element(115))
uuh=Button(root, text='Uuh', bg=sm, font=font, command=lambda:element(116))
uus=Button(root, text='Uus', bg=sm, font=font, command=lambda:element(117))

li=Button(root, text='Li', bg=sm, font=font, command=lambda:element(3))
na=Button(root, text='Na', bg=sm, font=font, command=lambda:element(11))
k=Button(root, text='K', bg=sm, font=font, command=lambda:element(19))
rb=Button(root, text='Rb', bg=sm, font=font, command=lambda:element(37))
cs=Button(root, text='Cs', bg=sm, font=font, command=lambda:element(55))
fr=Button(root, text='Fr', bg=sm, font=font, command=lambda:element(87))

'''
group1=Frame(root)
la=Button(group1, text='La', bg=sm, font=font, command=lambda:element(57))
ce=Button(group1, text='Ce', bg=sm, font=font, command=lambda:element(58))
pr=Button(group1, text='Pr', bg=sm, font=font, command=lambda:element(59))
nd=Button(group1, text='Nd', bg=sm, font=font, command=lambda:element(60))
pm=Button(group1, text='Pm', bg=sm, font=font, command=lambda:element(61))
sm=Button(group1, text='Sm', bg=sm, font=font, command=lambda:element(62))
eu=Button(group1, text='Eu', bg=sm, font=font, command=lambda:element(63))
gd=Button(group1, text='Gd', bg=sm, font=font, command=lambda:element(64))
tb=Button(group1, text='Tb', bg=sm, font=font, command=lambda:element(65))
dy=Button(group1, text='Dy', bg=sm, font=font, command=lambda:element(66))
ho=Button(group1, text='Ho', bg=sm, font=font, command=lambda:element(67))
er=Button(group1, text='Er', bg=sm, font=font, command=lambda:element(68))
tm=Button(group1, text='Tm', bg=sm, font=font, command=lambda:element(69))
yb=Button(group1, text='Yb', bg=sm, font=font, command=lambda:element(70))
lu=Button(group1, text='Lu', bg=sm, font=font, command=lambda:element(71))

group2=Frame(root)
ac=Button(group1, text='Ac', bg=sm, font=font, command=lambda:element(89))
tn=Button(group1, text='Tn', bg=sm, font=font, command=lambda:element(90))
pa=Button(group1, text='Pa', bg=sm, font=font, command=lambda:element(91))
u=Button(group1, text='U', bg=sm, font=font, command=lambda:element(92))
np=Button(group1, text='Np', bg=sm, font=font, command=lambda:element(93))
pu=Button(group1, text='Pu', bg=sm, font=font, command=lambda:element(94))
am=Button(group1, text='Am', bg=sm, font=font, command=lambda:element(95))
cm=Button(group1, text='Cm', bg=sm, font=font, command=lambda:element(96))
bk=Button(group1, text='Bk', bg=sm, font=font, command=lambda:element(97))
cf=Button(group1, text='Cf', bg=sm, font=font, command=lambda:element(98))
es=Button(group1, text='Es', bg=sm, font=font, command=lambda:element(99))
fm=Button(group1, text='Fm', bg=sm, font=font, command=lambda:element(100))
md=Button(group1, text='Md', bg=sm, font=font, command=lambda:element(101))
no=Button(group1, text='No', bg=sm, font=font, command=lambda:element(102))
lr=Button(group1, text='Lr', bg=sm, font=font, command=lambda:element(103))
'''

h.grid(row=1, column=1)
he.grid(row=1, column=18)

li.grid(row=2, column=1)
b.grid(row=2, column=13)
c.grid(row=2, column=14)
n.grid(row=2, column=15)
o.grid(row=2, column=16)
f.grid(row=2, column=17)
ne.grid(row=2, column=18)

na.grid(row=3, column=1)
ai.grid(row=3, column=13)
si.grid(row=3, column=14)
p.grid(row=3, column=15)
s.grid(row=3, column=16)
cl.grid(row=3, column=17)
ar.grid(row=3, column=18)

k.grid(row=4, column=1)
ga.grid(row=4, column=13)
ge.grid(row=4, column=14)
_as.grid(row=4, column=15)
se.grid(row=4, column=16)
br.grid(row=4, column=17)
kr.grid(row=4, column=18)

rb.grid(row=5, column=1)
_in.grid(row=5, column=13)
sn.grid(row=5, column=14)
sb.grid(row=5, column=15)
te.grid(row=5, column=16)
i.grid(row=5, column=17)
xe.grid(row=5, column=18)

cs.grid(row=6, column=1)
ti.grid(row=6, column=13)
pb.grid(row=6, column=14)
bi.grid(row=6, column=15)
po.grid(row=6, column=16)
at.grid(row=6, column=17)
rn.grid(row=6, column=18)

fr.grid(row=7, column=1)
uut.grid(row=7, column=13)
uuq.grid(row=7, column=14)
uup.grid(row=7, column=15)
uuh.grid(row=7, column=16)
uus.grid(row=7, column=17)
uuo.grid(row=7, column=18)

root.mainloop()