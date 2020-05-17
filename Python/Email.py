from tkinter import *
from imaplib import *
from tkinter import messagebox
import imaplib
import email
import ctypes
import getpass
import webbrowser

mail=IMAP4_SSL('imap.gmail.com',993)
check=False

def Set():
	if messagebox.askokcancel('Error',"The program can't run the email service because\nyour email don't give permission for other apps to use email\n\nPlease click OK to set this configuration on"):
		webbrowser.open_new('https://www.google.com/settings/security/lesssecureapps')

def Entries(event=None):
	us=eu.get()
	ps=ep.get()
	try:
		mail.login(us,ps)
		mail.select("INBOX")
		log.destroy()
		Main()
	except:
		Set()

def Loop():
	while True:
		n=0
		(code,mess)=mail.search(None,'(UNSEEN)')
		if code=='OK':
			for i in mess[0].split():
				n+=1
				typ,dat=mail.fetch(i,'(RFC822)')
				for res in dat:
					if isinstance(res,tuple):
						orig=email.message_from_string(res[1])
						txt=orig['From']+": "+orig['Subject']
						print(txt)
						posts.create_text(10,10,text=txt)

def Main():
	root=Tk()
	root.title('Email')
	root.geometry("400x300+100+100")

	posts=Canvas(root)

	root.mainloop()
	Loop()

def passhow():
	global check
	check=not check

	if check==False:
		ep['show']='*'
	if check==True:
		ep['show']=''

log=Tk()
log.title('Email')
log.geometry("200x200+100+100")
log.resizable(0,0)

Ch=IntVar()
eu=Entry(log)
ep=Entry(log, show='*')
sh=Checkbutton(log, text='Show Password', variable=Ch, onvalue=1, offvalue=0, command=passhow)
bl=Button(log, text='OK', command=Entries)

eu.grid(row=1, column=1)
ep.grid(row=2, column=1)
sh.grid(row=3, column=1)
bl.grid(row=4, column=1)

log.bind('<Return>', Entries)
log.mainloop()