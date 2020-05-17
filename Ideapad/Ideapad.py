from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config
import os
import webbrowser
import dropbox
import getpass
import platform

class Ideapad(App):
	sc=0
	cn=['']
	notes=['']
	note=0
	path=''
	current=''
	cfs=['C','D','E','F','G','A','B','Cm','Dm','Em','Fm','Gm','Am','Bm','C7','D7','E7','F7','G7','A7','B7','Cm7','Dm7','Em7','Fm7','Gm7','Am7','Bm7',\
	'C#','D#','E#','F#','G#','A#','B#','Cb','Db','Eb','Fb','Gb','Ab','Bb','C#m','D#m','E#m','F#m','G#m','A#m','B#m','Cbm','Dbm','Ebm','Fbm','Gbm','Abm','Bbm',\
	'C#7','D#7','E#7','F#7','G#7','A#7','B#7','Cb7','Db7','Eb7','Fb7','Gb7','Ab7','Bb7',]

	Window.size=(250,300)
	Window.resizable=(0,0)

	'''def on_start(self):
		sync=dropbox.Dropbox("aBESjwilnUAAAAAAAAAASm3YKU5MSXh1C5HreygrtqmDHsUCZ0Vltv4RePz2T-qf")
		sync.users_get_current_account()
		shlk=dropbox.files.SharedLink(url='https://www.dropbox.com/sh/r4ll0i7idt39k2r/AAAL6Wt8EaprRbglQF12Spqba?dl=0')
		auth=flow.start()
		webbrowser.open_new(auth)
		code=input(">")
		flow.finish(code.strip())
		sync.files_download_to_file('./Triskelion/Notes.db','./Notes.db')
		clt=dropbox.client.DropboxClient('aBESjwilnUAAAAAAAAAASm3YKU5MSXh1C5HreygrtqmDHsUCZ0Vltv4RePz2T')'''

	def new(self, btn):
		self.npop=GridLayout(cols=2)
		self.npopt=TextInput(multiline=False)
		self.npopb=Button(text='Ok', on_press=self.create, size_hint_x=None, width=60)
		self.npop.add_widget(self.npopt)
		self.npop.add_widget(self.npopb)
		self.pop=Popup(title='Name your file', size_hint_y=None, height=100, content=self.npop, auto_dismiss=False)
		self.pop.open()

	def create(self, btn):
		self.current=self.npopt.text+'.txt'
		self.notes.append(self.current)
		noteopen=open(self.path+"\\"+self.current,'w')
		self.tx.text=''
		noteopen.close()
		self.pop.dismiss()
		self.sm.current='pages'
		optxt=self.current[0:-4]
		if len(optxt)>20:
			optxt=optxt[0:17]
			optxt+='...'
		self.grm.remove_widget(self.grnw)
		self.grm.add_widget(Button(text=optxt, on_press=lambda *args, j=self.current: self.open(*args, j), size_hint_y=None, height=70))
		self.grm.add_widget(Button(text=':', on_release=self.poptions, size_hint_x=None, width=70, size_hint_y=None, height=70))
		self.grm.add_widget(self.grnw)
		self.grm.height+=70

	def open(self, btn, opn):
		self.current=opn
		noteopen=open(self.path+'\\'+self.current,'r')
		while True:
			n=noteopen.readline()
			if n=='<<END>>':
				self.sc=0
				break
			elif n=='<<NEXT>>\n':
				self.sc+=1
				self.cn.append('')
			else:
				self.cn[self.sc]+=n
		self.tx.text=self.cn[self.sc]
		noteopen.close()
		self.note=n
		self.sm.current='pages'

	def save(self, btn):
		self.cn[self.sc]=self.tx.text
		num=1
		noteopen=open(self.path+'\\'+self.current,'w')
		for i in self.cn:
			if i.endswith('\n'):
				i=i[0:-1]
			noteopen.write(i)
			if num!=len(self.cn):
				noteopen.write('\n<<NEXT>>\n')
				num+=1
		noteopen.write('\n<<END>>')
		#clt.put_file('./Triskelion/Notes.db',noteopen)
		noteopen.close()
		self.sm.current='notes'
		self.cn=['']
		self.sc=0

	def poptions(self, btn, opt):
		self.dpop=GridLayout(cols=1)
		self.dpop.add_widget(Button(text='rename', on_press=lambda *args, j=opt: self.rename_note(*args, j)))
		self.dpop.add_widget(Button(text='delete', on_press=lambda *args, j=opt: self.delete_note(*args, j)))
		self.dp=Popup(title='', size_hint_y=None, height=200,content=self.dpop, auto_dismiss=False)
		self.dp.open()

	def rename_note(self, btn, opt):
		self.dp.dismiss()
		self.npop=GridLayout(cols=2)
		self.npopt=TextInput(multiline=False)
		self.npopb=Button(text='Ok', on_release=self.create)
		self.npop.add_widget(self.npopt)
		self.npop.add_widget(self.npopb)
		self.pop=Popup(title='Rename your file', size_hint_y=None, height=100, content=self.npop, auto_dismiss=False)
		self.pop.open()

	def delete_note(self, btn, opt):
		self.grm.remove_widget(self.ids.opt)
		self.dp.dismiss()

	def previous(self, btn):
		if len(self.cn)-1<self.sc:
			self.cn.append(self.tx.text)
		else:
			self.cn[self.sc]=self.tx.text
		if self.sc>0:
			self.sc-=1
			self.tx.text=self.cn[self.sc]

	def add(self, btn):
		self.cn.append('')
		self.sc=len(self.cn)-1
		self.tx.text=''

	def delete(self, btn):
		if len(self.cn)>1:
			del(self.cn[self.sc])
			self.sc-=1
			self.tx.text=self.cn[self.sc]
		else:
			self.tx.text=''
			cn=['']

	def next(self, btn):
		if len(self.cn)-1<self.sc:
			self.cn.append(self.tx.text)
		else:
			self.cn[self.sc]=self.tx.text
		if self.sc<len(self.cn)-1:
			self.sc+=1
			self.tx.text=self.cn[self.sc]

	def cifra(self, btn):
		sel=select_text(int(self.tx.cursor_col)-2,int(self.tx.cursor_col)-1)
		if sel in self.cfs:
			self.tx.text+='\n'

	def build(self):

		#SCREENS
		self.sm=ScreenManager()
		self.s1=Screen(name='notes')
		self.s2=Screen(name='pages')

		#NOTES
		self.grm=GridLayout(cols=2, size_hint_y=None, height=140, padding=10)

		if platform.system()=='Windows':
			self.path='C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Notes'
		else:
			self.path='\\sdcard\\Triskelion\\Notes'

		for fil in os.listdir(self.path):
			self.notes.append(str(fil))
			optxt=fil[0:-4]
			if len(optxt)>20:
				optxt=optxt[0:17]
				optxt+='...'
			self.grm.add_widget(Button(text=optxt, id=fil, on_release=lambda *args, j=fil: self.open(*args, j), size_hint_y=None, height=70))
			self.grm.add_widget(Button(text=':', on_release=lambda *args, j=fil: self.poptions(*args, j), size_hint_x=None, width=70, size_hint_y=None, height=70))
			self.grm.height+=70
			self.note+=1
		self.grnw=Button(text='+', on_press=self.new, size_hint_y=None, height=70)
		self.grm.add_widget(self.grnw)

		self.scr=ScrollView(size_hint=(None,None), size=(Window.width, Window.height))
		self.scr.add_widget(self.grm)
		self.s1.add_widget(self.scr)

		#PAGES
		self.bp=Button(text='<', on_press=self.previous)
		self.ba=Button(text='+', on_press=self.add)
		self.bx=Button(text='X', on_press=self.delete)
		self.bs=Button(text='√', on_press=self.save)
		self.bn=Button(text='>', on_press=self.next)
		self.tx=TextInput(font_name='arial')

		self.gr=GridLayout(rows=2)
		self.sg=GridLayout(cols=5, height=30, size_hint=(1,None))
		self.sg.add_widget(self.bp)
		self.sg.add_widget(self.ba)
		self.sg.add_widget(self.bx)
		self.sg.add_widget(self.bs)
		self.sg.add_widget(self.bn)
		self.gr.add_widget(self.sg)
		self.gr.add_widget(self.tx)
		self.s2.add_widget(self.gr)

		#SHOW SCREENS
		self.sm.add_widget(self.s1)
		self.sm.add_widget(self.s2)
		self.sm.current='notes'
		#self.bind()
		return self.sm

if __name__=='__main__':
	Ideapad().run()