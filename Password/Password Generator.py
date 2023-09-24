from kivy.app import App
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from random import *
import pyperclip
import getpass
import time
import re


class MainScreen(App):

	Window.size=(260,400)
	Window.resizable=(0,0)

	chrs=['A','B','C,','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
	'1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	symb=['!','?','@','#','$','%','¨','&','*','-','_','+','=',';']
	psw={}
	plen=8
	sns=''

	def add(self, btn):
		if self.tad.text=='':
			self.tad.hint_text='Add a name to your password'
		else:
			if self.pas.text=='':
				self.psw[self.tad.text]=self.sns
			else:
				self.psw[self.tad.text]=self.pas.text
			self.box.add_widget(Button(text=self.tad.text, on_release=self.select, size_hint_y=None, height=40))
			self.box.height+=40
			fileopen=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Passwords.db','w')
			for key in self.psw:
				fileopen.write('[KEY]'+key+'\n')
				fileopen.write('[PASSWORD]'+self.psw[key]+'\n')
			fileopen.write('<<END>>\n')
			fileopen.close()

	def cle(self, btn):
		self.psw.clear()
		fileopen=open('Passwords.db','w')
		fileopen.write('<<END>>\n')
		fileopen.close()
		self.scl.remove_widget(self.box)
		self.box=GridLayout(cols=1, size_hint_y=None, height=80)
		self.scl.add_widget(self.box)

	def cop(self, btn):
		pyperclip.copy(self.sns)

	def password(self, btn):
		self.scm.current='Passwords'

	def back(self, btn):
		self.scm.current='Main'

	def generate(self, btn, c=False):
		self.plen=self.cen.text
		cif=''
		i=0

		if self.plen=='':self.plen=0
		elif re.search(r'\D', self.plen, re.I):
			self.plen=0
			self.cen.text='Invalid Input'
		else:self.plen=int(self.plen)
		if self.plen<8:self.plen=8
		if self.plen>20:self.plen=20

		if c==False:
			self.sns=''
			self.lb.text=''
		while i<self.plen:
			if self.csy.active==True:
				lis=self.chrs+self.symb
			else:
				lis=self.chrs
			s=round(randint(0,len(lis)-1))
			s=lis[s]
			if c==False:
				self.sns+=s
				i+=1
			if c==True:
				cif+=s
				i+=1
		if c==False:
			if self.csh.active==True:
				for i in self.sns:
					self.lb.text+=i
			if self.csh.active==False:
				for i in self.sns:
					self.lb.text+='*'
		if c==True:
			return cif

	def show(self, btn, v):
		self.lb.text=''
		for i in self.sns:
			if v:
				self.lb.text+=i
			else:
				self.lb.text+='*'

	def select(self, btn):
		self.lb.text=self.psw[btn.text]
		pyperclip.copy(self.psw[btn.text])
		self.scm.current='Main'

	def build(self):
		self.title='Password Generator'
		self.lb=Label(outline_color=[89, 89, 89])
		self.csy=CheckBox()
		self.csh=CheckBox()
		self.cyt=Label(text='Symbols')
		self.cht=Label(text='Show')

		self.scm=ScreenManager()
		self.s1=Screen(name='Main')
		self.s2=Screen(name='Passwords')

		self.psl=DropDown()
		for i in range(8,21):
			bl=Button(text=str(i), size_hint_y=None, height=44)
			bl.bind(on_release=lambda bl: self.psl.select(bl.text))
			self.psl.add_widget(bl)
		self.cen=Button(text='8', size_hint=(0.22, None), on_release=self.psl.open)
		self.psl.bind(on_select=lambda instance, x: setattr(self.cen, 'text', x))

		self.tad=TextInput(hint_text='Password Name', multiline=False)
		self.pas=TextInput(hint_text='Custom Password', multiline=False)
		self.bad=Button(text='Add', on_release=self.add)
		self.bcr=Button(text='Clear', on_release=self.cle)
		self.bcp=Button(text='Copy', on_release=self.cop)
		self.bps=Button(text='Passwords', on_release=self.password)
		self.bgn=Button(text='Generate', on_release=self.generate)

		self.sps=GridLayout(cols=1)
		self.sps.add_widget(Button(text='<', on_release=self.back, size_hint_y=None, height=30))
		self.scl=ScrollView(size_hint_y=None, size=(Window.width, Window.height))
		self.box=GridLayout(cols=1, size_hint_y=None, height=80)
		
		fileopen=open('Passwords.db','r')
		while True:
			n=fileopen.readline()
			if n=='<<END>>\n':break
			else:self.psw[n[5:-1]]=fileopen.readline()[10:-1]
		fileopen.close()
		for key in self.psw:
			self.box.add_widget(Button(text=key, on_release=self.select, size_hint_y=None, height=40))
			self.box.height+=40

		self.scl.add_widget(self.box)
		self.sps.add_widget(self.scl)
		self.s2.add_widget(self.sps)

		self.cfg=GridLayout(cols=2)
		self.cfg.add_widget(self.cen)
		self.cfg.add_widget(self.tad)

		self.chk=GridLayout(cols=4)
		self.chk.add_widget(self.cyt)
		self.chk.add_widget(self.csy)
		self.chk.add_widget(self.cht)
		self.chk.add_widget(self.csh)

		self.bts=GridLayout(cols=4, height=30, size_hint=(1,None))
		self.bts.add_widget(self.bad)
		self.bts.add_widget(self.bcr)
		self.bts.add_widget(self.bcp)
		self.bts.add_widget(self.bps)

		self.gr=GridLayout(cols=1)
		self.gr.add_widget(self.lb)
		self.gr.add_widget(self.chk)
		self.gr.add_widget(self.cfg)
		self.gr.add_widget(self.pas)
		self.gr.add_widget(self.bts)
		self.gr.add_widget(self.bgn)
		self.s1.add_widget(self.gr)

		self.csh.bind(active=self.show)
		self.scm.add_widget(self.s1)
		self.scm.add_widget(self.s2)
		self.scm.current='Main'
		return self.scm

if __name__=='__main__':
	MainScreen().run()