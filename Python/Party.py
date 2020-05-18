from colorama import *
from random import randint
import time
from getpass import getpass
import os

class Game():
	def __init__(self):
		self.play = True
		self.players = ['','','','']
		self.steps = [0,0,0,0]
		self.score = [0,0,0,0]
		self.boards = [[4,8,14,19,25],[2,8,13,17,24,28],[5,9,13,15,20,24,29],[1,3,7,11,15,18,23,27],[3,8,12,21,29]]
		self.brd = []
		self.quest = [[],[],[],[]]
		
		self.plen = 0
		self.slen = 0
		self.turn = 0
		self.nb = 0
		
		for i in range(4):
			file = open('Quest' + str(i + 1) + '.db','r')
			while True:
				l = file.readline()
				if l[:-1] == '*':
					lst = []
					lst.append(file.readline()[:-1])
					lst.append(file.readline()[:-1])
					lst.append(file.readline()[:-1])
					lst.append(file.readline()[:-1])
					lst.append(file.readline()[:-1])
					lst.append(file.readline()[:-1])
					self.quest[i].append(lst.copy())
				else: break
			file.close()
	
	def start_screen(self):
		print(Fore.GREEN)
		print('《■■■□■■■□■■■□■■■□■□■》')
		print('《■□■□■□■□■□■□□■□□■□■》')
		print('《■■■□■■■□■■□□□■□□■■■》')
		print('《■□□□■□■□■□■□□■□□□■□》')
		print(Style.RESET_ALL)
		
		while self.plen not in ('2','3','4'):
			self.plen = input('JOGADORES: ')
			if self.plen == '': self.plen = 4; break
		self.plen = int(self.plen)
		
		for i in range(self.plen):
			self.players[i] = input('JOGADOR ' + str(i + 1) + ': ')
			if self.players[i] == '':
				if i == 0: self.players[i] = '♤'
				if i == 1: self.players[i] = '♡'
				if i == 2: self.players[i] = '♧'
				if i == 3: self.players[i] = '◇'
		
		while self.slen not in ('1','2','3','4','5','6','7','8','9','0'):
			self.slen = input('PONTOS: ')
			if self.slen == '': self.slen = 3; break
		self.slen = int(self.slen)
		
		for i in range(self.plen):
			self.brd.append(self.boards[round(randint(0,4))])
		
	def dice(self, max):
		getpass('\n' + Fore.YELLOW + self.players[self.turn] + ' Jogue o Dado! ')
		self.nb = round(randint(1,max))
		print('= ' + str(self.nb) + Style.RESET_ALL)
		time.sleep(0.5)
	
	def board_show(self):
		for pl in range(self.plen):
			path =''
			if pl == self.turn: path += Fore.YELLOW
			path += self.players[pl] + ': ' + str(self.score[pl]) + ' '
			if self.steps[pl] > 0:
				for i in range(self.steps[pl]):
					if i - 1 in self.brd[pl]: path += '□'
					else: path += '○'
			
			if self.steps[pl] - 1 in self.brd[pl]: path += '■'
			else: path += '●'
			
			for i in range(30 - self.steps[pl]):
				if i + self.steps[pl] in self.brd[pl]: path += '□'
				else: path += '○'
			if pl == self.turn: path += Style.RESET_ALL
					
			print(path)
			
	def quiz_show(self):
		os.system('clear')
		self.board_show()
		print('\n' + Fore.CYAN + 'HORA DO QUIZ!')
		self.dice(4)
		if self.nb == 1: print(Fore.CYAN + '\nArtes' + Style.RESET_ALL)
		elif self.nb == 2: print(Fore.CYAN + '\nCiências' + Style.RESET_ALL)
		elif self.nb == 3: print(Fore.CYAN + '\nHistória' + Style.RESET_ALL)
		elif self.nb == 4: print(Fore.CYAN + '\nPop' + Style.RESET_ALL)
		self.nb -= 1
		
		qz = round(randint(0,len(self.quest[self.nb]) - 1))
		lpt = ['$' + self.quest[self.nb][qz][1]]
		for i in self.quest[self.nb][qz][2:-1]:
			lpt.append('#' + i)
		
		opt = []
		i = 4
		while i > 0:
			p = round(randint(0,len(lpt) - 1))
			opt.append(lpt[p])
			del lpt[p]
			i -= 1
			
		for i in range(len(opt)):
			if opt[i][0] == '$':
				rans = str(i + 1)
				break
		
		print('\n' + self.quest[self.nb][qz][0] + '\n')
		print('1) ' + opt[0][1:])
		print('2) ' + opt[1][1:])
		print('3) ' + opt[2][1:])
		print('4) ' + opt[3][1:] + '\n')
		print('d) Dica\n')
		ans = ''
		while ans not in ('1','2','3','4'):
			ans = input('> ')
			if ans == 'd':
				print(self.quest[self.nb][qz][5])
		
		if ans == rans:
			print(Fore.GREEN + '\nResposta certa!' + Style.RESET_ALL)
			self.score[self.turn] += 1
		else: print(Fore.RED + '\nResposta errada...' + Style.RESET_ALL)
		time.sleep(0.5)
	
	def main(self):
		os.system('clear')
		self.board_show()
		time.sleep(0.2)
		
		if self.score[self.turn] < self.slen:
			self.dice(6)
			self.steps[self.turn] += self.nb
			
			if self.steps[self.turn] > 30:
				self.steps[self.turn] = 0
			os.system('clear')
			self.board_show()
			time.sleep(0.5)
				
			if self.steps[self.turn] - 1 in self.brd[self.turn]:
				self.quiz_show()
		
		if self.score[self.turn] == self.slen:
			os.system('clear')
			self.board_show()
			print('\n' + Fore.GREEN + '☆ ' + self.players[self.turn] + ' GANHOU! ☆')
			
			time.sleep(0.5)
			
			print(Style.RESET_ALL)
			print('Jogar de novo? [s/n]')
			sn = ''
			while sn not in ('s','n'): sn = input('> ')
			if sn == 's':
				for i in range(self.plen):
					self.steps[i] = 0
				for i in range(self.slen):
					self.score[i] = 0
				self.turn = -1
			else:
				os.system('clear')
				print('Obrigado por jogar!\n- Matt Kai -\n')
				time.sleep(0.5)
				self.play = False
				
		self.turn += 1
		if self.turn == self.plen: self.turn = 0

g = Game()
g.start_screen()
while g.play == True:
	g.main()