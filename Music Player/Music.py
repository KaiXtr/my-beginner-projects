import os
import pygame
from tkinter import *
from random import *
from tkinter import messagebox
from threading import Thread
import mutagen
import eyed3
#import magic
import time
import tkinter.filedialog

playnow=[]
songs=[]
tracks=[]
artists=[]
albums=[]
playlists=[['In Bloom.mp3','Dumb.mp3'],['Heart Shaped Box.mp3','Lithium.mp3']]
ct=0
index=0
mlen=0
clen=0
tlen=0
slen=0
showbox=False
showmode=1
songis="Stoped"
shf=False
fade=False
repeat=0
times=2
AU=0

#Data
file=open('JukeboxData.db','r')
folder=file.readline()
file.close

#Functions
class runtime(Thread):
	def run(self):
		global repeat
		global index
		global mlen
		global clen
		global tlen
		global slen
		global times
		global AU

		while tlen<slen:
			time.sleep(1)
			if songis!="Playing":
				break
			tlen+=1
			clen+=1
			if clen==60:
				mlen+=1
				clen=0
			if clen<10:
				curtime["text"]=str(mlen)+":0"+str(clen)
			else:
				curtime["text"]=str(mlen)+":"+str(clen)
		if tlen==slen:
			if repeat==0:
				if index<len(songs)-1:
					bnext(None)
					runtime().start()
			if repeat==1:
				bnext(None)
				runtime().start()
			if repeat==2:
				pygame.mixer.music.play()
				updatelabel()
			if repeat==3:
				if AU!=times:
					AU+=1
					pygame.mixer.music.play()
					updatelabel()
					runtime().start()
				else:
					AU=0
					bnext(None)

def updatelabel():
    global index
    global l_track
    global l_artist
    global l_album
    global album_artwork
    global mlen
    global clen
    global tlen
    global slen

    alb=mutagen.File(songs[index])
    #if alb.tags['APIC:']!="":
	#    artwork=alb.tags['APIC:'].data
	#    with open('image.jpg', 'wb') as img:
	#    	img.write(artwork) 
    #album_artwork["image"]=img

    slen=int(alb.info.length)
    box.itemconfig(index, {'bg':'aqua'})

    m=0
    s=0
    i=0
    mlen=0
    clen=0
    tlen=0
    while i<slen:
        s+=1
        if s==60:
            m+=1
            s=0
        i+=1
    if s<10:
        s="0"+str(s)
    curtime["text"]="0:00"
    lentime["text"]=str(m)+":"+str(s)
    root.title(tracks[index]+' - Jukebox')
    v.set(tracks[index])
    a.set(artists[index])
    l.set(albums[index])
    if len(tracks[index])>20:
        l_track['font']='arial 13 bold'
    else:
        l_track['font']='arial 15 bold'

def bprevious(event):
	global index
	global songis
	global tlen
	global slen
	global mlen

	if tlen==0:
		box.itemconfig(index, {'bg':'gray'})
		if index>=0:
			index-=1
		if index<0:
			index=len(playnow)-1
		if songis!="Playing":
			runtime().start()
			b_play.grid_forget()
			b_pause.grid(row=1,column=1)
		pygame.mixer.music.load(playnow[index])
		pygame.mixer.music.play()
		box.itemconfig(index, {'bg':'aqua'})
	elif tlen>0:
		pygame.mixer.music.rewind()
		mlen=0
		clen=0
		tlen=0

	songis="Playing"
	updatelabel()

def bplay(event):
	global songis

	if songis=="Stoped":
		pygame.mixer.music.play()
	if songis=="Paused":
		pygame.mixer.music.unpause()
	b_play.grid_forget()
	b_pause.grid(row=1,column=1)
	songis="Playing"
	runtime().start()

def splay(e):
	global playnow
	global songis
	global index
	global showmode

	w=e.widget
	if showmode==1:
		box.itemconfig(index, {'bg':'gray'})
		index=int(w.curselection()[0])
		if songis!="Playing":
			runtime().start()
			b_play.grid_forget()
			b_pause.grid(row=1,column=1)
		pygame.mixer.music.load(playnow[index])
		pygame.mixer.music.play()
		box.itemconfig(index, {'bg':'aqua'})
		songis="Playing"
		updatelabel()
	if showmode>1:
		fil(showmode+6,w.get(w.curselection()[0]))

def bpause(event):
	global songis
	pygame.mixer.music.pause()
	b_pause.grid_forget()
	b_play.grid(row=1,column=1)
	songis="Paused"

def bstop(event):
	global songis
	global mlen
	global clen
	global tlen

	mlen=0
	clen=0
	tlen=0
	if fade==True:
		pygame.mixer.music.fadeout(1500)
	if fade==False:
		pygame.mixer.music.stop()
	b_pause.grid_forget()
	b_play.grid(row=1,column=1)
	songis="Stoped"
	updatelabel()

def bnext(event):
	global index
	global songis
	global repeat
	global shf
	global fade

	box.itemconfig(index, {'bg':'gray'})
	if index<len(playnow)-1:
		if shf==False:
			index+=1
		if shf==True:
			index=(round(randint(1,len(playnow))))-1
			print(index)
			if index==-1:
				index=0
	elif index==len(playnow)-1:
		index=0
	if songis!="Playing":
		runtime().start()
		b_play.grid_forget()
		b_pause.grid(row=1,column=1)
	songis="Playing"
	pygame.mixer.music.load(playnow[index])
	pygame.mixer.music.play()
	updatelabel()

def rshuffle(event):
	global shf
	shf=not shf

	if shf==False:
		r_shuffle['image']=shoffimg
	if shf==True:
		r_shuffle['image']=shonimg

def rrepeat(event):
	global repeat
	global times
	repeat+=1
	if repeat==4:
		repeat=0
	if repeat==0:
		r_repeat['image']=repoffimg
	if repeat==1:
		r_repeat['image']=reponimg
	if repeat==2:
		r_repeat['image']=reposongimg
	if repeat==3:
		r_repeat['image']=repo3img

def rfade(event):
	global fade
	fade=not fade

	if fade==False:
		r_fade['image']=fadeoffimg
	if fade==True:
		r_fade['image']=fadeonimg

def rshow(event):
	global showbox
	showbox=not showbox

	if showbox==False:
		filters.grid_forget()
		box.grid_forget()
		f_son.grid_forget()
		f_art.grid_forget()
		f_alb.grid_forget()
		f_yea.grid_forget()
		f_ply.grid_forget()
		root.geometry("250x250+100+100")
		r_shw['image']=showoffimg
	if showbox==True:
		filters.grid(row=5, column=0, columnspan=3)
		box.grid(row=1, column=0, rowspan=5)
		f_son.grid(row=1, column=1)
		f_art.grid(row=2, column=1)
		f_alb.grid(row=3, column=1)
		f_ply.grid(row=4, column=1)
		f_yea.grid(row=5, column=1)
		root.geometry("250x405+100+100")
		r_shw['image']=showonimg

def directory():
	global index
	global folder

	if folder=="":
		folder=tkinter.filedialog.askdirectory()
		file=open('JukeboxData.db','w')
		file.write(folder)
		file.close()
	os.chdir(folder)

	for files in os.listdir(folder):
		if files.endswith(".mp3"):
			redir=os.path.realpath(files)
			try:
				audio=eyed3.load(redir)

				if audio.tag.title!="":
					tracks.append(audio.tag.title)
				else:
					tracks.append(files)

				if audio.tag.artist!="":
						artists.append(audio.tag.artist)
				else:
					artists.append("Unknown Artist")

				if audio.tag.album!="":
					albums.append(audio.tag.album)
				else:
					albums.append("Songs")
			except:
				tracks.append(files)
				artists.append("Unknown Artist")
				albums.append("Songs")

			songs.append(files)
			playnow.append(files)
			index+=1

	if len(songs)==0:
		messagebox.showinfo("Error", " There is no MP3 songs in this folder, \n Please try again.")
		directory()

	songs.sort()
	# tracks.sort()
	playnow.sort()
	songs.reverse()
	tracks.reverse()
	playnow.reverse()
	for items in tracks:
		box.insert(0,items)
	songs.reverse()
	tracks.reverse()
	playnow.reverse()
	index=0
	updatelabel()

def fil(f, i=0):
	global showmode
	global index
	box.delete(0, END)
	c=0

	if f==1:
		songs.reverse()
		for items in songs:
			box.insert(0,items)
		songs.reverse()
	if f==2:
		artists.reverse()
		for items in artists:
			if items not in box.get(0,END):
				box.insert(0,items)
		artists.reverse()
	if f==3:
		albums.reverse()
		for items in albums:
			if items not in box.get(0,END):
				box.insert(0,items)
		albums.reverse()
	if f==4:
		playlists.reverse()
		for items in playlists:
			box.insert(0,items)
		playlists.reverse()
	if f==8:
		playnow.clear()
		tracks.clear()
		songs.reverse()
		artists.reverse()
		while c<len(songs):
			if artists[c]==i:
				playnow.append(songs[c])
				tracks.append(songs[c])
				box.insert(0,songs[c])
			c+=1
		songs.reverse()	
		playnow.reverse()
		tracks.reverse()
		artists.reverse()
	if f==9:
		playnow.clear()
		tracks.clear()
		songs.reverse()
		albums.reverse()
		while c<len(songs):
			if albums[c]==i:
				playnow.append(songs[c])
				tracks.append(songs[c])
				box.insert(0,songs[c])
			c+=1
		songs.reverse()
		playnow.reverse()
		tracks.reverse()
		albums.reverse()
	if f==10:	
		while c<len(playlists[i]):
			songs.pop(c)
			tracks.pop(c)
			songs.append(playlists[i][c])
			tracks.append(playlists[i][c])
			box.insert(0,playlists[i][c])
			c+=1
	if showmode<6:
		showmode=f
	if showmode>5:
		showmode=1
		index=0

def endapp():
	pygame.mixer.music.stop()
	pygame.mixer.quit()
	root.destroy()

#Window
root=Tk()
root.title("Jukebox")
root.geometry("250x250+100+100")
root.resizable(0,0)
root["bg"]='#00001A'

#Labels
v=StringVar()
a=StringVar()
l=StringVar()
img=PhotoImage(file='Icons/Apple.png')
repbar=Frame(root)
curtime=Label(repbar, text=0)
lentime=Label(repbar, text=0)
info=Frame(root, bg='#FF9900')
album_artwork=Label(root, width=50, image=img)
l_track=Label(root, bg='#FF9900', textvariable=v, width=20, font='arial 15 bold')
l_artist=Label(root, bg='#FF9900', textvariable=a, width=35)
l_album=Label(root, bg='#FF9900', textvariable=l, width=35)

#Buttons
flson=PhotoImage(file='Icons/SONGS.png')
flart=PhotoImage(file='Icons/ARTISTS.png')
flalb=PhotoImage(file='Icons/ALBUMS.png')
flyea=PhotoImage(file='Icons/YEARS.png')
flply=PhotoImage(file='Icons/PLAYLISTS.png')
flfol=PhotoImage(file='Icons/FOLDERS.png')
flgen=PhotoImage(file='Icons/GENDERS.png')
filters=Frame(root, bg='#333333')
box=Listbox(filters, bg="gray", relief=FLAT)
f_son=Button(filters, image=flson, relief=FLAT, bg='#333333', command=lambda:fil(1))
f_art=Button(filters, image=flart, relief=FLAT, bg='#333333', command=lambda:fil(2))
f_alb=Button(filters, image=flalb, relief=FLAT, bg='#333333', command=lambda:fil(3))
f_ply=Button(filters, image=flply, relief=FLAT, bg='#333333', command=lambda:fil(4))
f_yea=Button(filters, image=flyea, relief=FLAT, bg='#333333', command=lambda:fil(5))
f_fol=Button(filters, image=flfol, relief=FLAT, bg='#333333', command=lambda:fil(6))
f_gen=Button(filters, image=flgen, relief=FLAT, bg='#333333', command=lambda:fil(7))

primg=PhotoImage(file='Icons/Previous.png')
plimg=PhotoImage(file='Icons/Play.png')
psimg=PhotoImage(file='Icons/Pause.png')
stimg=PhotoImage(file='Icons/Stop.png')
nximg=PhotoImage(file='Icons/Next.png')
buttons=Frame(root, bg='#00001A')
b_prev=Button(buttons, image=primg, relief=FLAT, bg='#00001A', activebackground='darkblue')
b_play=Button(buttons, image=plimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
b_pause=Button(buttons, image=psimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
b_stop=Button(buttons, image=stimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
b_next=Button(buttons, image=nximg, relief=FLAT, bg='#00001A', activebackground='darkblue')

shonimg=PhotoImage(file='Icons/ShuffleON.png')
shoffimg=PhotoImage(file='Icons/ShuffleOFF.png')
reponimg=PhotoImage(file='Icons/RepeatON.png')
repoffimg=PhotoImage(file='Icons/RepeatOFF.png')
reposongimg=PhotoImage(file='Icons/RepeatSONG.png')
repo3img=PhotoImage(file='Icons/Repeat3.png')
fadeonimg=PhotoImage(file='Icons/FadeON.png')
fadeoffimg=PhotoImage(file='Icons/FadeOFF.png')
showonimg=PhotoImage(file='Icons/ShowON.png')
showoffimg=PhotoImage(file='Icons/ShowOFF.png')
reprodution=Frame(root)
r_shuffle=Button(reprodution, image=shoffimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
r_repeat=Button(reprodution,  image=repoffimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
r_fade=Button(reprodution,  image=fadeoffimg, relief=FLAT, bg='#00001A', activebackground='darkblue')
r_shw=Button(reprodution,  image=showoffimg, relief=FLAT, bg='#00001A', activebackground='darkblue')

#Positions
album_artwork.grid(row=0,column=0)
repbar.grid(row=1,column=0)
curtime.grid(row=1,column=1)
lentime.grid(row=1,column=3)

info.grid(row=2,column=0,columnspan=3)
l_track.grid(row=2,column=0)
l_artist.grid(row=3,column=0)
l_album.grid(row=4,column=0)

buttons.grid(row=6,column=0)
b_prev.grid(row=1,column=0)
b_play.grid(row=1,column=1)
b_stop.grid(row=1,column=2)
b_next.grid(row=1,column=3)

reprodution.grid(row=7,column=0)
r_shuffle.grid(row=0,column=0)
r_repeat.grid(row=0,column=1)
r_fade.grid(row=0,column=2)
r_shw.grid(row=0,column=3)

#Bindings
b_prev.bind("<Button-1>",bprevious)
b_play.bind("<Button-1>",bplay)
b_pause.bind("<Button-1>",bpause)
b_stop.bind("<Button-1>",bstop)
b_next.bind("<Button-1>",bnext)
r_shuffle.bind("<Button-1>",rshuffle)
r_repeat.bind("<Button-1>",rrepeat)
r_fade.bind("<Button-1>",rfade)
r_shw.bind("<Button-1>",rshow)
box.bind("<<ListboxSelect>>",splay)

directory()
pygame.mixer.init()
pygame.mixer.music.load(songs[index])
root.protocol("WM_DELETE_WINDOW", endapp)
root.mainloop()