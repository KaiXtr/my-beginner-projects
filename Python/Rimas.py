from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size=(350,200)
Window.resizable=(0,0)

class MainScreen(App):

	ão=['alemão','botão','brasão','cão','chão','coração','direção','dragão','então','mão','não','pão','razão','são','solidão','tão','trovão']
	al=['animal','astral','central','legal','mal','natural','surreal']
	ar=['amar','falar','mar','olhar','rimar','andar','cansar','celular','cantar','dançar','escutar','estar','acertar','já','inovar','popular','abandonar','derrubar','ajudar','esperar','mudar','chorar','devagar','levantar','impressionar']
	ade=['ansiedade','calamidade','felicidade','liberdade','mentalidade','curiosidade','cidade','universidade','saudade']
	ado=['manipulado','alienado','lado','controlado','apaixonado']
	ais=['fatais','gerais','generais','navais','cais','mais','jamais','atrás','pais','demais']
	am=['disseram','eram']
	az=['capaz','paz']
	ei=['esperei','decorei','sonhei','falei','olhei','andei','encontrei','sei','viajei','vacilei']
	êlo=['camelo','cabelo']
	élo=['belo','chinelo']
	em=['alguém','bem','ninguém','sem','também','tem',]
	ez=['vez']
	ente=['de repente','diferente','ente','quente']
	er=['dizer','porque','conhecer','correr','ler','beber','comer','esquecer','você','viver','sofrer','perder','ser','esconder','ver','saber','querer']
	eu=['apareceu','escondeu','esqueceu','eu']
	ir=['ir','partir','sair','sentir']
	igo=['domingo','comingo','amigo','abrigo']
	im=['mim','ruim','assim']
	ismo=['comunismo','capitalismo','liberalismo','ambientalismo','machismo','feminismo','ocultismo','cristianismo','niilismo','vitimismo']
	osto=['gosto','oposto','rosto']
	ória=['glória','vitória']
	ôr=['amor','dor','perdedor','professor','vencedor']
	ou=['abandonou','acordou','começou','funcionou','passou']

	def findrime(self, btn):
		self.inp=self.tx.text
		self.lb.text=''

		if (self.inp.endswith("ão")) or (self.inp in self.ão):
			self.lis=self.ão
		if (self.inp.endswith("al")) or (self.inp in self.al):
			self.lis=self.al
		if (self.inp.endswith("ar")) or (self.inp in self.ar):
			self.lis=self.ar
		if (self.inp.endswith("ade")) or (self.inp in self.ade):
			self.lis=self.ade
		if (self.inp.endswith("ado")) or (self.inp in self.ado):
			self.lis=self.ado
		if (self.inp.endswith("ais")) or (self.inp in self.ais):
			self.lis=self.ais
		if (self.inp.endswith("am")) or (self.inp in self.am):
			self.lis=self.am
		if (self.inp.endswith("az")) or (self.inp in self.az):
			self.lis=self.az
		if (self.inp.endswith("ei")) or (self.inp in self.ei):
			self.lis=self.ei
		if (self.inp.endswith("elo")) or (self.inp in self.élo):
			self.lis=self.élo
		if (self.inp.endswith("em")) or (self.inp in self.em):
			self.lis=self.em
		if (self.inp.endswith("ez")) or (self.inp in self.ez):
			self.lis=self.ez
		if (self.inp.endswith("ente")) or (self.inp in self.ente):
			self.lis=self.ente
		if (self.inp.endswith("er")) or (self.inp in self.er):
			self.lis=self.er
		if (self.inp.endswith("eu")) or (self.inp in self.eu):
			self.lis=self.eu
		if (self.inp.endswith("ir")) or (self.inp in self.ir):
			self.lis=self.ir
		if (self.inp.endswith("igo")) or (self.inp in self.igo):
			self.lis=self.igo
		if (self.inp.endswith("im")) or (self.inp in self.im):
			self.lis=self.im
		if (self.inp.endswith("ismo")) or (self.inp in self.ismo):
			self.lis=self.ismo
		if (self.inp.endswith("osto")) or (self.inp in self.osto):
			self.lis=self.osto
		if (self.inp.endswith("ória")) or (self.inp in self.ória):
			self.lis=self.ória
		if (self.inp.endswith("or")) or (self.inp in self.ôr):
			self.lis=self.ôr
		if (self.inp.endswith("ou")) or (self.inp in self.ou):
			self.lis=self.ou

		self.lis.reverse()
		for i in self.lis:
			self.lb.text+=i+'\n'

	def build(self):
		self.title='Rimas'
		self.tx=TextInput(multiline=False)
		self.lb=Label(text='')
		self.bt=Button(text='Find Rime')
		self.bt.bind(on_release=self.findrime)

		self.gr=GridLayout(cols=1)
		self.gr.add_widget(self.tx)
		self.gr.add_widget(self.lb)
		self.gr.add_widget(self.bt)

		return self.gr

if __name__=='__main__':
	MainScreen().run()