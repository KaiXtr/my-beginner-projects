import os
import re
import time
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

#FUNCTIONS
def login():
	global log
	n=1
	log=len(users)+1
	pas=''
	for i in users:
		print(str(n)+' > '+i[0])
		n+=1
	print('+ > new\nX > exit\n')
	while True:
		log=input('=')
		if log=='+':
			signin()
			break
		elif log=='X':
			break
		elif int(log) <= len(users):
			signup()
			break

def signin():
	global log
	log=len(users)
	print('\nWhat is your name?')
	nam=input('=')
	print('\nHow old are you?')
	age=input('=')
	print('\nCreate your password')
	pas=input('=')
	print('\nConfirm your password')
	while True:
		con=input('=')
		if con==pas: break
	users.append([])
	users[len(users)-1].append(nam)
	users[len(users)-1].append(age)
	users[len(users)-1].append(con)
	print('\nDone!')
	time.sleep(1)
	os.system('clear')
	print('Welcome, '+nam)
	
def signup():
	global log
	global pas
	log=int(log)-1
	print('\nPASSWORD')
	while True:
		pas=input('=')
		if pas!=users[log][2]:
			print(Fore.RED+"\nACCESS DENIED:"+Style.RESET_ALL)
		else:
			print(Fore.GREEN+'\nACCESS GRANTED'+Style.RESET_ALL)
			time.sleep(1)
			os.system('clear')
			if int(time.strftime('%H'))>=0 and int(time.strftime('%H'))<12:
				print("\nGood Morning, "+users[log][0]+'\n')
			elif int(time.strftime('%H'))>11 and int(time.strftime('%H'))<19:
				print("\nGood Afternoon, "+users[log][0]+'\n')
			elif int(time.strftime('%H'))>18 and int(time.strftime('%H'))<=24:
				print("\nGood Night, "+users[log][0]+'\n')
			break

#LOADING FILES
users=[]
file=open('accounts.db','r')
i=0
while True:
	n=file.readline()
	if n!='END':
		users.append([])
		users[i].append(n[0:-1])
		users[i].append(file.readline()[0:-1])
		users[i].append(file.readline()[0:-1])
		i+=1
	else:
		break
file.close()
print(Fore.GREEN + 'Hello World!\n' + Style.RESET_ALL)
time.sleep(1)
login()
		
#MAIN
diary=''
draw=''
while log!='X':
	print()
	fun=input('=')
	
	if re.search('bye', fun, re.IGNORECASE):
		print('\nSee you later, '+users[log][0]+'\n')
		time.sleep(1)
		os.system('clear')
		login()
	
	elif re.search('cmd', fun, re.IGNORECASE):
		os.system(fun[3:])
		
	elif re.search(r"\d['+','-','*','/','x','÷','×']\d", fun, re.I):
		try:
			fun=fun.replace('x','*')
			fun=fun.replace('×','*')
			fun=fun.replace('÷','/')
			print("The result is "+str(eval(fun)))
		except:
			print('?')
			
	elif re.search('time', fun, re.IGNORECASE):
		print(Fore.CYAN+time.strftime('%H:%M')+Style.RESET_ALL)
		
	elif re.search('date', fun, re.IGNORECASE):
		print(Fore.CYAN+time.strftime('%d/%m/%y')+Style.RESET_ALL)
		
	elif re.search('draw', fun, re.IGNORECASE):
		os.system('clear')
		print(Fore.RED+'1 - RED\n'+Fore.YELLOW+'2 - YELLOW\n'+Fore.GREEN+'3 - GREEN\n'+Fore.CYAN+'4 - CYAN\n'+Fore.BLUE+'5 - BLUE\n'+Fore.MAGENTA+'6 - MAGENTA\n'+Style.RESET_ALL+'7 - WHITE\nX - exit\n')
		w=''
		while w!='X':
			w=input('')
			if w=='1':print(Fore.RED)
			elif w=='2':print(Fore.YELLOW)
			elif w=='3':print(Fore.GREEN)
			elif w=='4':print(Fore.CYAN)
			elif w=='5':print(Fore.BLUE)
			elif w=='6':print(Fore.MAGENTA)
			elif w=='7':print(Style.RESET_ALL)
			draw+=w+'\n'
		os.system('clear')
		draw=draw[0:-2]
		print(draw+Style.RESET_ALL)
		
	elif re.search('status', fun, re.IGNORECASE):
		print(os.system('/proc/cpuinfo'))
		
	elif re.search('info', fun, re.IGNORECASE):
		print('NAME: '+users[log][0])
		print('AGE: '+users[log][1])
		
	elif re.search('name', fun, re.IGNORECASE):
		print('Input your new name:')
		nam=input('=')
		users[log][0]=nam
		print('Done, '+users[log][0])
		
	elif re.search('age', fun, re.IGNORECASE):
		print('Input your new age:')
		age=input('=')
		users[log][1]=age
		print('Done, you are '+users[log][1]+' years old')
		
	elif re.search('write', fun, re.IGNORECASE):
		print('input X to exit\n')
		w=''
		while w!='X':
			w=input('')
			diary+=w+'\n'
		diary=diary[0:-2]
		print('\nInput file name:')
		fin=input('=')
		if fin!='':
			file=open(fin,'w')
			file.write(diary)
			file.close()
		else: print(Fore.RED+'Not saved'+Style.RESET_ALL)
		
	elif re.search('read', fun, re.IGNORECASE):
		print('\nInput file name:')
		fin=input('=')
		try:
			file=open(fin,'r')
			print('\n'+file.read()+'\n')
			file.close()
		except: print(Fore.RED+"\nCan't find "+fin+'\n'+Style.RESET_ALL)
		
	elif re.search('delete', fun, re.IGNORECASE):
		print('Are you sure? [ y/n ]')
		yn=input('=')
		if yn=='y':
			print('Goodbye, '+users[log][0]+'\n')
			time.sleep(1)
			os.system('clear')
			users=users[0:-1]
			login()
	
#SAVE
file=open('accounts.db','w')
i=0
while i<len(users):
	file.write(users[i][0]+'\n')
	file.write(users[i][1]+'\n')
	file.write(users[i][2]+'\n')
	i+=1
file.write('END')
file.close()