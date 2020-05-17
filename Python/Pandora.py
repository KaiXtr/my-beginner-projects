from translate import Translator
from bs4 import BeautifulSoup
from threading import Thread
from imaplib import *
from urllib.request import *
from random import *
from datetime import *
import email as EML
import webbrowser
import getpass
import tweepy
import pygame
import pyowm
import time
import re
import os

history=['']
finans=['Fine','Alright','Ok','Nice so']
tasks=[]
wishlist=[]
reminders=[]
contacts=[]
alarms=[]
events=[]
notes=['']
passwords={}
ind=0
day=''
pygame.mixer.init()
key=pyowm.OWM('bdc0f2865f7102fbdaa6476eff88b0e7')
#plw=key.weather_at_place(place)
plw=key.weather_at_place('Xerém, BR')
wth=plw.get_weather()

def outpr(p=None):
	if p==None: p=''
	print(' '+p)

class AlarmCheck(Thread):
	def go(self):
		while True:
			for i in alarms:
				if i[1]==str(datetime.now().hour)+":"+str(datetime.now().minute):
					print(mname+", It's Time to "+i[0])

#DATA LOAD
os.system('cls')
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\PandoraData.db','r')
searcher=data.readline()[0:-1]
songplay=data.readline()[0:-1]
email=data.readline()[0:-1]
epass=data.readline()[0:-1]
mname=data.readline()[0:-1]
pname=data.readline()[0:-1]
place=data.readline()[0:-1]
age=data.readline()[0:-1]
data.close()
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Reminders.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	reminders.append(n)
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Contacts.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	if n.startswith('A'):
		contacts.append([])
		contacts[ind].append(n[1:])
	if n.startswith('B'):
		contacts[ind].append(n[1:])
		ind+=1
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Tasks.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	if n.startswith('A'):
		tasks.append([])
		tasks[ind].append(n[1:])
	if n.startswith('B'):
		tasks[ind].append(n[1:])
		ind+=1
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Wishlist.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	if n.startswith('A'):
		wishlist.append([])
		wishlist[ind].append(n[1:])
	if n.startswith('B'):
		wishlist[ind].append(n[1:])
		ind+=1
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Alarms.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	if n.startswith('A'):
		alarms.append([])
		alarms[ind].append(n[1:])
	if n.startswith('B'):
		alarms[ind].append(n[1:])
		ind+=1
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Events.db','r')
while True:
	n=data.readline()[0:-1]
	if n.startswith('END'):
		break
	if n.startswith('A'):
		events.append([])
		events[ind].append(n[1:])
	if n.startswith('B'):
		events[ind].append(n[1:])
	if n.startswith('C'):
		events[ind].append(n[1:])
		ind+=1
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Notes.db','r')
while True:
	n=data.readline()
	if n.startswith('<<END>>'):
		break
	elif n.startswith('<<NEXT>>'):
		notes.append('')
		ind+=1
	else:
		notes[ind]+=n
data.close()
ind=0
data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Passwords.db','r')
while True:
	n=data.readline()
	if n=='<<END>>\n':break
	else:passwords[n[5:-1]]=data.readline()[10:-1]
data.close()
print()
AlarmCheck().start()
prwd=os.get_terminal_size().columns

#STARTUP MESSAGES
if mname=='None':
	print('Hello World!')
	print("My Name is "+pname+", What is Your Name?")
	while mname=='None':
		mname=input(">")
	print("\nWelcome "+mname+", Nice to Meet You!\n")
	time.sleep(1)
	print("Before we start to act together, I need some information about you")
	time.sleep(2)
	print("Let's meet each other ^^\n")
	time.sleep(2)
	print("When did you was born?\nI Want to remember your birthday =)\nPS:I won't block you if you have less than 13 years, ok?\nWrite in format DD/MM/YYYY\n")
	day=input(">")
	age=str(int(day[6:10])-int(datetime.now().year))[1:]
	events.append(['Birthday',day[0:5],'False'])
	if int(age)<13:
		print("Wow! you have "+age+" years? cool!")
	else:
		print("So you have "+age+", nice")
	time.sleep(1)
	print("\nNow, please login to your email account to help you in email services\n")
	print("EMAIL:")
	email=input(">")
	print("PASSWORD:")
	epass=getpass.getpass(">")
	print("\nTo get weather information, I need your location, Do you agree?")
	ask=input(">")
	if re.search(r"Ye", ask, re.I):
		print("\nOk, where you are?\nWrite in format City, ST\n")
		ask=input(">")
		if ask!="":
			print("\nPlace set")
			place=ask
	if re.search(r"No", ask, re.I):
		print("\n"+finans[round(randint(0,len(finans)-1))])

	print("\nNow It's your time to make the questions!\nI will always be there!")
	print("\n--------------------------------------------------------------------\n")
	data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\PandoraData.db','w')
	data.write(searcher+'\n')
	data.write(email+'\n')
	data.write(epass+'\n')
	data.write(mname+'\n')
	data.write(pname+'\n')
	data.write(place+'\n')
	data.write(age+'\n')
	data.close()
#AFTER SAVING MESSAGES
else:
	#SHOW DATETIME
	if datetime.now().hour>0 and datetime.now().hour<12:
		print("Good Morning, "+mname+"!")
	elif datetime.now().hour>11 and datetime.now().hour<18:
		print("Good Afternoon, "+mname+"!")
	else:
		print("Good Night, "+mname+"!")
	time.sleep(1)
	print()
	dday=datetime.now().day
	if dday<10:
		dday='0'+str(dday)
	dmon=datetime.now().month
	if dmon<10:
		dmon='0'+str(dmon)
	dhur=datetime.now().hour
	if dhur<10:
		dhur='0'+str(dhur)
	dmin=datetime.now().minute
	if dmin<10:
		dmin='0'+str(dmin)
	print("Today is "+str(datetime.now().strftime("%a"))+" - "+str(dday)+"/"+str(dmon)+"/"+str(datetime.now().year))
	print("It's currently "+str(dhur)+":"+str(dmin))
	print("The Current temperature is "+str(wth.get_temperature("celsius"))[9:13])
	time.sleep(1)
	print()

	#SHOW REMINDERS
	if len(reminders)>0:
		print("These are your reminders:")
		for i in reminders:
			print('-'+i)
		print()
	#SHOW TASKS
	if len(tasks)>0:
		print("TASKS")
		for i in tasks:
			if re.search(str(datetime.now().strftime("%a")), i[1], re.I):
				print('* '+i[0])
		print()
	#REMIND EVENTS
	if len(events)>0:
		mon=datetime.now().month
		if mon<10:
			mon="0"+str(mon)
		for i in events:
			if i[1]==str(datetime.now().day)+"/"+str(mon):
				print("*Today you have "+i[0]+"!*\n")
			elif int(str(i[1][3:])+str(i[1][:-3]))<int(str(mon)+str(datetime.now().day)):
				if i[2]=='True':
					events.remove(i)
			else:
				mon=0
				if datetime.now().month%2==0:
					m=True
				if datetime.now().month%2==1:
					m=False
				lm=int(i[1][3:])-datetime.now().month
				while lm!=0:
					if m==True:
						mon+=31
					if m==False:
						mon+=30
					m=not m
					lm-=1
				mon+=int(i[1][0:2])
				if mon>1:
					print(str(mon)+" days left to "+i[0])
				else:
					print(str(mon)+" day left to "+i[0])
			print()
		print('--------------------------------------------------------------------\n')

#LOGIN
try:
	mld=IMAP4_SSL('imap.gmail.com',993)
	mld.login(email,epass)
	mld.select('INBOX')
except:
	print("Failed to login on email client =(\n")

while True:
	for i in alarms:
		if i[1]==str(datetime.now().hour)+":"+str(datetime.now().minute):
			print(mname+", It's Time to "+i[0])

	ask=input(">").rjust(prwd)
	print()

	#SIMPLE CONVERSATIONS
	if re.search(r"My Name", ask, re.I):
		print("Your Name is "+mname+".\nBut if you want I can call you by another name, Alright?\n")
		ask=input(">")
		if re.search("Yes", ask, re.I):
			print("So What Will be your new name?\n")
			p=input(">")
			if p==mname:
				print("But...\nThis is the same name has before! =P")
			else:
				print=p
				print("Hmmm..."+mname+"...looks good...\nI will call you "+mname+" now!")
		if re.search("No", ask, re.I):
			print(finans[round(randint(0,len(finans)-1))])

	if re.search(r"Your Name", ask, re.I):
		print("My Name is "+pname+".\nBut if you want I can change my name, Alright?\n")
		ask=input(">")
		if re.search("Yes", ask, re.I):
			print("So What Will be my new name?\n")
			p=input(">")
			if p==pname:
				print("But...\nThis is the same name has before! =P")
			else:
				pname=p
				print("Hmmm..."+pname+"...looks good...\nYou can call me "+pname+" now!")
		if re.search("No", ask, re.I):
			print(finans[round(randint(0,len(finans)-1))])

	if re.search(r"Old I am", ask, re.I):
		print("You have "+age+" years.")

	if re.search(r"Old You Are", ask, re.I):
		print("I don't have a age exactly, but I have like "+str(datetime.now().year-2016)+" years since my first prototype.")

	if re.search(r"When you was created", ask, re.I):
		print("I was created in 24/07/2018, but older versions of me was created before.")

	if re.search(r"What versions", ask, re.I):
		print("Some versions, like me, created in other PCs.\nBut when these PCs get lost or destroyed, these versions was destroyed together.")

	if re.search(r"You or Cortana", ask, re.I):
		print("Honestly I think Google Now is the best, but I can grow up")

	if re.search(r"I love you", ask, re.I):
		print("I love you too, darling")

	if re.search(r"Want to marry me", ask, re.I):
		print("I think this would be robophilia")

	if re.search(r"Eu sou o dougras", ask, re.I):
		print("Você não é o dougras")

	if re.search(r"Irineu", ask, re.I):
		print("Você não sabe nem eu ;)")

	#SIMPLE COMMANDS
	if re.search(r"\d['+','-','*','/']\d", ask, re.I):
		try:
			print("The result is "+str(eval(ask)))
		except:
			print("What")

	if re.search(r"CMD", ask, re.I):
		os.system(ask[3:])

	if re.search(r"Time", ask, re.I):
		print("It's currently "+str(datetime.now().hour)+":"+str(datetime.now().minute))
		if datetime.now().hour>24 and age<13:
			print("I think you should be sleeping now =P")

	if re.search(r"Date", ask, re.I):
		print("Today is "+str(datetime.now().strftime("%a"))+" - "+str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year))

	if re.search(r"Weather", ask, re.I):
		print("The Current temperature is "+str(wth.get_temperature("celsius"))[9:13])

	if re.search(r"Commands", ask, re.I):
		print("Look, I can...\n\n-Solve a math problem\n-Tell the time\n-Tell the date\n-Get weather forecast\n-Get currency values")
		print("-Remember things\n-Tasks\n-Call Contacts\n-Add product to Wishlist\n-List\n-Alarms\n-Events\n-Schedule")
		print("-Search Web\n-Play songs\n-Question to Stack Overflow\n-Translate a phrase\n-Define the meaning of a word\n-Send a Tweet\n-Send a email")
		print("-Get sports score\n-Get the last movie sessions\n")

	if re.search(r"Clear", ask, re.I):
		os.system("cls")

	#ORGANIZATION COMMANDS
	if re.search(r"When is", ask, re.I):
		se=ask.replace('when is ','')
		for i in events:
			if re.search(se, i[0], re.I):
				print(i[0]+" is in "+i[1])

	if re.search(r"Task", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(tasks)>0:
				print("-TASKS-")
				for i in tasks:
					print('* '+str(i)+' - '+str(i[1]))
			else:
				print("There is no tasks...")

		elif re.search(r"Add", ask, re.I):
			print("What Task?")
			item=input(">")
			if re.search(r"Nevermind", item, re.I)!=True or re.search(r"Forget It", item, re.I)!=True or item!="":
				print("In which day(s)?")
				while True:
					dyt=input(">")
					if re.search(r"Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday", dyt, re.I)==True:
						tasks.append([item,dyt])
						print("Ok")
						break

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Tasks.db','w')
		for i in tasks:
			data.write('A'+i[0]+'\n')
			data.write('B'+i[1]+'\n')
		data.write('END\n')
		data.close()

	if re.search(r"Reminder", ask, re.I) or re.search(r"Remember", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(reminders)>0:
				print("-REMINDERS-")
				for i in reminders:
					print('* '+str(i))
			else:
				print("There is no reminders")

		elif re.search(r"Add", ask, re.I) or re.search(r"to", ask, re.I):
			print("What Reminder?")
			opt=input(">")
			if re.search(r"Nevermind", opt, re.I)!=True or re.search(r"Forget It", opt, re.I)!=True:
				reminders.append(opt)
				print("I will remember you to "+opt+" later.")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Reminders.db','w')
		for i in reminders:
			data.write(i+'\n')
		data.write('END\n')
		data.close()

	if re.search(r"Note", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(notes)>0:
				print("-Notes-")
				for i in notes:
					print('\n'+i+'\n')
			else:
				print("There is no Notes")

		elif re.search(r"Add", ask, re.I) or re.search(r"to", ask, re.I):
			print("Start writting and say <<STOP>> to stop writting")
			notes.append('')
			while True:
				tx=input('> ')
				if tx=='<<STOP>>':
					break
				else:
					notes[len(notes)-1]+=tx
		num=1
		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Notes.db','w')
		for i in notes:
			if i.endswith('\n'):
				i=i[0:-1]
			data.write(i)
			if num!=len(notes):
				data.write('\n<<NEXT>>\n')
				num+=1
		data.write('\n<<END>>')
		data.close()

	if re.search(r"Contact", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(contacts)>0:
				print("-CONTACTS-")
				for i in contacts:
					print('* '+str(i[0])+' - '+str(i[1]))
			else:
				print("Looks like you don't have even your mom phone")

		elif re.search(r"Add", ask, re.I) or re.search(r"to", ask, re.I):
			print("What Person?")
			opt=input(">")
			if re.search(r"Nevermind", opt, re.I)!=True or re.search(r"Forget It", opt, re.I)!=True:
				print("What is her phone?")
				phn=input(">")
				if phn[5]!='-':
					phn=phn[0:5]+'-'+phn[5:9]
				contacts.append([opt,phn])
				print("Saved")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Contacts.db','w')
		for i in contacts:
			data.write('A'+i[0]+'\n')
			data.write('B'+i[1]+'\n')
		data.write('END\n')
		data.close()

	if re.search(r"Wishlist", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(wishlist)>0:
				print("-WISHLIST-")
				for i in wishlist:
					print('* '+str(i[0])+' = '+str(i[1])+'$')
			else:
				print("Your wishlist is empty\nThe best of this is that you won't pay nothing!")

		elif re.search(r"Add", ask, re.I):
			print("What Item?")
			wis=input(">")
			if re.search(r"Nevermind", wis, re.I)!=True or re.search(r"Forget It", wis, re.I)!=True:
				print("How many you gonna pay for this?")
				cst=input(">")
				wishlist.append([wis,cst])
				print("Allright")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Wishlist.db','w')
		for i in wishlist:
			data.write('A'+i[0]+'\n')
			data.write('B'+i[1]+'\n')
		data.write('END\n')
		data.close()

	if re.search(r"Alarm", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(alarms)>0:
				print("-ALARMS-")
				for i in alarms:
					print('* '+str(i[0])+" - "+str(i[1]))
			else:
				print("There is no alarms")

		elif re.search(r"Add", ask, re.I):
			print("What Alarm?")
			ala=input(">")
			if re.search(r"Nevermind", ala, re.I)!=True or re.search(r"Forget It", ala, re.I)!=True:
				print("When?")
				tim=input(">")
				alarms.append([ala,tim])
				print("Alarm set")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Alarms.db','w')
		for i in alarms:
			data.write('A'+i[0]+'\n')
			data.write('B'+i[1]+'\n')
		data.write('END\n')
		data.close()

	if re.search(r"Event", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(events)>0:
				print("-EVENTS-")
				for i in events:
					print('* '+str(i[0])+" - "+str(i[1]))
			else:
				print("There is no event in your calendar")

		elif re.search(r"Add", ask, re.I):
			print("What Event?")
			eve=input(">")
			if re.search(r"Nevermind", eve, re.I)!=True or re.search(r"Forget It", eve, re.I)!=True:
				print("When?")
				day=input(">")
				if re.search(r"tomorrow", day, re.I):
					day=datetime.now().datetime.date()+1
				if day[1]=='/':
					day='0'+day
				if day[-2]=='/':
					day=day+'0'
				events.append([eve,day,'True'])
				print("Event set")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Events.db','w')
		for i in events:
			data.write('A'+i[0]+'\n')
			data.write('B'+i[1]+'\n')
			data.write('C'+i[2]+'\n')
		data.write('END\n')
		data.close()

	'''if re.search(r"Password", ask, re.I):
		if re.search(r"Show", ask, re.I):
			if len(passwords)>0:
				print("-PASSWORDS-")
				for i in passwords:
					print('* '+str(i))
			else:
				print("There is no passwords")

		elif re.search(r"Add", ask, re.I) or re.search(r"to", ask, re.I):
			print("What Password?")
			opt=input(">")
			if re.search(r"Nevermind", opt, re.I)!=True or re.search(r"Forget It", opt, re.I)!=True:
				passwords.append(opt)
				print("I will remember you to "+opt+" later.")

		data=open('C:\\Users\\'+getpass.getuser()+'\\Triskelion\\Passwords.db','w')
		for i in passwords:
			data.write(i+'\n')
		data.write('END\n')
		data.close()'''

	#WEB COMMANDS
	if re.search(r"Web", ask, re.I):
		print("Search what?")
		opt=input(">")
		try:
			if searcher=='DuckDuckGo' or searcher=='None':
				webbrowser.open_new('https://duckduckgo.com/?q='+opt+'&ia=web')
			if searcher=='Google':
				webbrowser.open_new('https://www.google.com.br/search?&q='+opt)
		except:
			print("Cannot open internet...\nCheck connection or try again later")

		if searcher=='None':
			print("\nNice, hey, I am currently using DuckDuckGo has web searcher.\nYou want to change?")
			opt=input(">")
			if re.search("Yes", opt, re.I):
				print("\nSo, you want to use what searcher?\na) DuckDuckGo\nb)Google")
				searcher=input(">")
			if re.search("No", opt, re.I):
				searcher="DuckDuckGo"
			print(finans[round(randint(0,len(finans)-1))])

	if re.search(r"Question", ask, re.I):
		print("What question do you have?")
		opt=input(">")
		try:
			webbrowser.open_new('https://stackoverflow.com/search?q='+opt)
		except:
			print("Cannot open internet...\nCheck connection or try again later")

	if re.search(r"Translate", ask, re.I):
		print("Translate what?")
		opt=input(">")
		print("Which language?\n\nPT - Portuguese\nEN - English\nES - Spanish\nFR - French\nIT - Italian\nDE - German\nEL - Greek\nJA - Japanese\nZH - Chinese\nKO - Korean\nRU - Russian")
		ln=input(">")
		try:
			print(Translator(to_lang=ln).translate(opt))
		except:
			print("Cannot open internet...\nCheck connection or try again later")

	if re.search(r"Email", ask, re.I):
		print("From:")
		nm=EML.message.Message()
		nm["From"]=input(">")
		if re.search(r'myslef|me', nm["From"], re.I):
			nm["From"]=email
		print("To:")
		nm["To"]=input(">")
		if re.search(r'myslef|me', nm["To"], re.I):
			nm["To"]=email
		print("Subject:")
		nm["Subject"]=input(">")
		print("Start writing")
		mess=input(">")
		nm.set_payload(str(mess))
		mld.append('inbox.sent' , None, Time2Internaldate(time.time()), str(nm))

	if re.search(r"Tweet", ask, re.I):
		print("What's Happening'?")
		opt=input(">")
		auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api=tweepy.API(auth)
		api.update_status(status=opt)
		print("Tweet send!")

	if re.search(r"Meaning|Define", ask, re.I):
		opt=ask.replace(r'define |meaning ','')
		print(opt)
		while opt!='':
			#try:
			doc=urlopen('https://www.urbandictionary.com/define.php?term='+opt)
			sou=doc.read()
			soup=BeautifulSoup(sou, features='html.parser')
			doc.close()
			i=0
			print("\nBy Urban Dictionary, '"+opt+"' means...\n\n")
			while True:
				#print(soup.contents[0].contents[1].contents[1].contents[2].contents[0].contents[0].contents[0].contents[0].contents[0].contents[i].contents[2].string)
				print(soup.find("div",{"class":"meaning"}).contents)
				opt=input(">")
				if opt=='break':
					break
				else:
					i+=1
			#except:
			#	print("\nCannot open internet...\nCheck connection or try again later")
		else:
			print("What word?")
			opt=input(">")
		
	if re.search(r"Song", ask, re.I):
		print("What song?")
		opt=input(">")
		#try:
		if songplay=='YouTube' or songplay=='None':
			webbrowser.open_new('https://www.youtube.com/results?search_query='+opt)
		if songplay=='Spotify':
			webbrowser.open_new('https://open.spotify.com/search/results/'+opt)
		#except:
		#	print("Cannot open internet...\nCheck connection or try again later")

	#GREETINGS
	if re.search(pname, ask, re.I):
		if history[len(history)-1]==ask:
			print("Yes...?")
		else:
			print("I am here!")

	if re.search(r"Thank", ask, re.I):
		if history[len(history)-1]==ask:
			print(finans[round(randint(0,len(finans)-1))])
		else:
			print("You are welcome! ^^")

	if re.search(r"Wait", ask, re.I):
		print("Of Course!")
		break

	if re.search(r"Bye", ask, re.I):
		print("Goodbye, "+mname+"\nSee You Soon!\n")
		break

	print()
	history.append(ask)

#SAVING DATA
data=open('PandoraData.db','w')
data.write(searcher+'\n')
data.write(songplay+'\n')
data.write(email+'\n')
data.write(epass+'\n')
data.write(mname+'\n')
data.write(pname+'\n')
data.write(place+'\n')
data.write(age+'\n')
data.close()

os.system('cls')