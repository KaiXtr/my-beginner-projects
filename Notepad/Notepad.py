from tkinter import *
from tkinter import ttk
import os as OS
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
from threading import Thread
import matplotlib.font_manager
import webbrowser
import time

text=["Untitled"]
lan="English"
b=False
i=False
o=False
u=False
a=1
tls=True
title=False
linumb=True
filna=""
abquant=0
abindex=0
col=False
readonly=True
auto=0
auco=True
bckp=False
thme=1
indent=1

recent=[]
tabfil=[]
ind=0

#Funções
class autosave(Thread):
    def run(self):
        global auto
        t=0
        while auto>0:
            time.sleep(1)
            t+=1
            if t>=auto and auto!=0 and text[abquant]!="Untitled":
                t=0
                sav()
                if lan=="English":
                    ls["text"]='File Saved'
                if lan=="Português":
                    ls["text"]='Arquivo Salvo'
                if lan=="Español":
                    ls["text"]='Archivo Guardado'
                time.sleep(3)
                ls["text"]=""

class run(Thread):
    def run(self):
        global filna
        #OS.system("start cmd")
        if filna.endswith('.bas')==True:
            OS.system("fbc "+filna)
            OS.system("start "+filna[0:-3]+".exe")
        if filna.endswith('.py')==True:
            OS.system("python "+filna)
        if filna.endswith('.html')==True:
            webbrowser.open_new(filna)
        else:
            OS.system("start "+filna)

class CustomText(Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, intag=False, start="1.0", end="end", regexp=False):

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            if intag==True:
                index=self.search('<'+pattern, "matchEnd","searchLimit", count=count, regexp=regexp)
            if intag==False:
                index=self.search(pattern, "matchEnd","searchLimit", count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

def tabs(t,r,b=False):
    global filna
    global readonly
    global recent
    global ind
    global title
    global abquant

    filna=str(OS.path.split(t)[1])
    if (t not in recent) and (r==True):
        recent.append(t)
        hist.add_command(label=filna, command=lambda val=ind:opnrec(val))
        ind+=1
    if (t not in text) and (b==False):
        ab.append(ttk.Frame(abas))
        abas.add(ab[abquant], text=filna)
        ab[abquant].rowconfigure(0, weight=300)
        ab[abquant].columnconfigure(1, weight=300)
        tabfil.append(t)
        if abquant>0:
            lines.append(Canvas(ab[abquant], width=20))
            scroll.append(Text(ab[abquant], width=1000, height=3000, borderwidth=0, wrap=None))
            barx.append(Scrollbar(ab[abquant], orient='horizontal', command=scroll[abquant].xview, cursor='arrow'))
            bary.append(Scrollbar(ab[abquant], orient='vertical', command=scroll[abquant].yview, cursor='arrow'))
            scroll[abquant].config(font=fn, xscrollcommand=barx[abquant].set, yscrollcommand=bary[abquant].set)
            barl.append(Label(ab[abquant]))
            lines[abquant].grid(row=0, column=0, sticky=N+S)
            scroll[abquant].grid(row=0, column=1, sticky=N+S+W+E)
            barx[abquant].grid(row=2, column=1, sticky=W+E)
            bary[abquant].grid(row=0, column=2, sticky=N+S)
            barl[abquant].grid(row=2, column=2, sticky=N+S+W+E)
            i=0
            while i<1000:
                lines[abquant].create_text(1,i*19,text=i,anchor=N+W)
                i+=1
            print(ab)
            print(scroll)

def tabch(e=None):
    global abindex
    abindex=abas.index('current')
    update()
    titleshow(False)

def new():
    global text

    if scroll[abquant].get('1.0', END + '-1c')!='':
        if lan=="English":
            if messagebox.askyesno("Save", "Do You Wish to Save Changes?")==True:
                savas()
        if lan=="Português":
            if messagebox.askyesno("Salvar", "Deseja Salvar Alterações?")==True:
                savas()
        if lan=="Español":
            if messagebox.askyesno("Salvar", "Desea Salvar Cambios?")==True:
                savas()
    text.pop(abquant)
    titleshow(s=False)
    scroll[abquant].delete('1.0',END)

def create():
    new()
    savas()

def opn():
    global text
    global abquant
    global abindex

    if text[abquant]!="Untitled":
        abquant+=1
    else: 
        text=[]
    f=filedialog.askopenfile(parent=janela, mode='rb', title='Choose the file to open', defaultextension="*.*", 
    filetypes=(("Text Files", "*.txt"), ("Rich Text Files", "*.rtf"), ("Batch Files", "*.bat"), ("Basic Files", "*.bas"), ("Binary Files", "*.bin"), ("Database Files", "*.db"),
    ("Dinamic Link Libraries Files", "*.dll"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("C Files", "*.c"), ("Javascript Files", "*.js"),
    ("Java Files", "*.jar"), ("Python Files", "*.py"), ("LUA Files", "*.lua"), ("All Files", "*.*")))
    if f!=None and f!="Untitled":
        if readonly==False:
            scroll[abquant].config(state='normal')
        tabs(str(f.name),True)
        text.append(str(f.name))
        contents=f.read()
        print(scroll)
        print(abquant)
        scroll[abquant].delete('1.0', END)
        scroll[abquant].insert('1.0', contents)
        f.close()
        if readonly==False:
            scroll[abquant].config(state='normal')
    update()
    savedata()
    if title==True:
        titleshow(False)

def opnrec(r):
    global abquant
    global ablen
    global recent
    global text

    if recent[r].endswith('\n')==True:
        recent[r]=recent[r][0:-1]

    if readonly==False:
        scroll[abquant].config(state='normal')

    if text[abquant]!="Untitled":
        abquant+=1
    else:
        text=[]
    #try:
    fileopen=open(recent[r], 'r')
    contents=fileopen.read()
    scroll[abquant].delete('1.0', END)
    scroll[abquant].insert('1.0', contents)
    fileopen.close()
    #except:
    #    messagebox.showerror("Can't find "+str(OS.path.split(recent[r])),'Looks like this file was renamed or even deleted')
    tabs(recent[r],False)
    if recent[r] not in text:
        text.append(str(recent[r]))
    if readonly==False:
        scroll[abquant].config(state='disabled')
    update()
    if title==True:
        titleshow(False)

def upopn():
    global text
    data=scroll[abquant].get('1.0', END + '-1c')
    y=open(text.name,'w')
    y.write(data)
    y.close()

def sav():
    global text
    if text[abquant]!="Untitled":
        data=scroll[abquant].get('1.0', END + '-1c')
        y=open(text[abquant],'w')
        y.write(data)
        y.close()
    else:
        savas()

def savas():
    global text
    global bckp
    global abindex

    f=filedialog.asksaveasfile(mode='w', title='Choose where to save the file', defaultextension=".txt",
    filetypes=(("Text Files", "*.txt"), ("Rich Text Files", "*.rtf"), ("Batch Files", "*.bat"), ("Basic Files", "*.bas"),  ("Binary Files", "*.bin"), ("Database Files", "*.db"),
    ("Dinamic Link Libraries Files", "*.dll"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("C Files", "*.c"), ("Javascript Files", "*.js"),
    ("Java Files", "*.java"), ("Python Files", "*.py"), ("LUA Files", "*.lua"), ("All Files", "*.*")))
    if bckp==True:
        pass
    if f!=None:
        tabs(f.name,True,b=True)
        filna=str(OS.path.split(f.name)[1])
        data=scroll[abindex].get('1.0', END + '-1c')
        y=open(text[abindex],'w')
        y.write(data)
        y.close()
    savedata()

def printer():
    if text.name.endswith(".txt"):
        OS.startfile(text.name, "print")
    else:
        filna=str(OS.path.split(text.name)[1])
        OS.startfile(filna, "print")

def clo():
    global abquant
    global text

    print(text[abquant])
    new()
    if abquant==0:
        filna=str(OS.path.split(text[abquant].name)[1])
        abas.add(ab[0], text=filna)
    else:
        abas.forget(ab[abquant])
        abquant-=1

def qut():
    savedata()
    if lan=="English":
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            janela.destroy()
    if lan=="Português":
        if messagebox.askokcancel("Sair", "Tem certeza que quer sair?"):
            janela.destroy()
    if lan=="Español":
        if messagebox.askokcancel("Salir", "Seguro que quieres salir?"):
            janela.destroy()

def colorpicker():
    def colorset(event=None):
        c=''
        if len(en.get())<6:
            l=6-len(en.get())
            while len(c)<l:
                c+='0'
        c+=en.get()
        if len(c)>6:
            c=c[0:5]
        en['bg']='#'+c

    cl=Tk()
    cl.title('Color Picker')
    cl.geometry('300x200+400+400')
    cl.resizable(0,0)

    c=0
    en=Entry(cl)
    en.grid(row=0, column=0)

    cl.bind('<Key>', colorset)
    cl.mainloop()

def abo():
    if lan=="English":
        l=messagebox.showinfo("About", " Program by KaiXtr \n Made in Sublime Text \n Tkinter Graphic Module \n 24/11/2017")
    if lan=="Português":
        l=messagebox.showinfo("Sobre", " Programa por KaiXtr \n Criado no Sublime Text \n Módulo Gráfico Tkinter \n 24/11/2017")
    if lan=="Español":
        l=messagebox.showinfo("Sobre", " Programa por KaiXtr \n Hecho in Sublime Text \n Módulo Gráfico Tkinter \n 24/11/2017")

def lang(l):
    global lan

    if l=="English":
        if lan!='English':
            janela.title('Notepad')
            bar.entryconfigure('Editar', label='Edit')
            file.entryconfigure('Abrir', label='Open')
            file.entryconfigure('Salvar', label='Save')
            file.entryconfigure('Salvar Como', label='Save as')
            file.entryconfigure('Imprimir', label='Print')
            view.entryconfigure('Idioma', label='Language')
            view.entryconfigure('Tema', label='Theme')
            help.entryconfigure('Sobre...', label='About...')
            ausa.entryconfigure('Nunca', label='Never')
            ausa.entryconfigure('1 Minuto', label='1 Minute')
            ausa.entryconfigure('5 Minutos', label='5 Minutes')

            if lan=='Português':
                bar.entryconfigure('Arquivo', label='File')
                bar.entryconfigure('Exibir', label='View')
                bar.entryconfigure('Ajuda', label='Help')
                file.entryconfigure('Novo', label='New')
                file.entryconfigure('Criar', label='Create')
                file.entryconfigure('Abrir Recente', label='Open Recent')
                file.entryconfigure('Atualizar', label='Update')
                file.entryconfigure('Executar', label='Run')
                file.entryconfigure('Fechar', label='Close')
                file.entryconfigure('Sair', label='Quit')
                view.entryconfigure('Mostrar nome do arquivo', label='Show file name')
                view.entryconfigure('Mostrar linhas numeradas', label='Show line numbers')
                view.entryconfigure('Palavras coloridas', label='Colored words')
                edit.entryconfigure('Modo Leitura', label='Read Only')
                edit.entryconfigure('Paleta de Cores', label='Color Picker')
                ausa.entryconfigure('Sempre', label='Always')

            if lan=='Español':
                bar.entryconfigure('Archivo', label='File')
                bar.entryconfigure('Vista', label='View')
                bar.entryconfigure('Ayuda', label='Help')
                file.entryconfigure('Nuevo', label='New')
                file.entryconfigure('Crear', label='Create')
                file.entryconfigure('Abrir Reciente', label='Open Recent')
                file.entryconfigure('Actualizar', label='Update')
                file.entryconfigure('Correr', label='Run')
                file.entryconfigure('Cercar', label='Close')
                file.entryconfigure('Salir', label='Quit')
                view.entryconfigure('Mostrar nombre de archivo', label='Show file name')
                view.entryconfigure('Mostrar número de líneas', label='Show line numbers')
                view.entryconfigure('Palabras coloreadas', label='Colored words')
                edit.entryconfigure('Modo de Lectura', label='Read Only')
                edit.entryconfigure('Paleta de Colores', label='Color Picker')
                ausa.entryconfigure('Siempre', label='Always')

            lan="English"
            titleshow(s=False)
    if l=="Português":
        if lan!='Português':
            janela.title('Bloco de Notas')

            if lan=='English':
                bar.entryconfigure('File', label='Arquivo')
                bar.entryconfigure('Edit', label='Editar')
                bar.entryconfigure('View', label='Exibir')
                bar.entryconfigure('Help', label='Ajuda')
                file.entryconfigure('New', label='Novo')
                file.entryconfigure('Create', label='Criar')
                file.entryconfigure('Open', label='Abrir')
                file.entryconfigure('Open Recent', label='Abrir Recente')
                file.entryconfigure('Update', label='Atualizar')
                file.entryconfigure('Save', label='Salvar')
                file.entryconfigure('Save as', label='Salvar Como')
                file.entryconfigure('Print', label='Imprimir')
                file.entryconfigure('Run', label='Executar')
                file.entryconfigure('Close', label='Fechar')
                file.entryconfigure('Quit', label='Sair')
                view.entryconfigure('Theme', label='Tema')
                view.entryconfigure('Language', label='Idioma')
                help.entryconfigure('About...', label='Sobre...')
                view.entryconfigure('Show file name', label='Mostrar nome do arquivo')
                view.entryconfigure('Show line numbers', label='Mostrar linhas numeradas')
                view.entryconfigure('Colored words', label='Palavras coloridas')
                edit.entryconfigure('Read Only', label='Modo Leitura')
                edit.entryconfigure('Color Picker', label='Paleta de Cores')
                ausa.entryconfigure('Never', label='Nunca')
                ausa.entryconfigure('1 Minute', label='1 Minuto')
                ausa.entryconfigure('5 Minutes', label='5 Minutos')
                ausa.entryconfigure('Always', label='Sempre')

            if lan=='Español':
                bar.entryconfigure('Archivo', label='Arquivo')
                bar.entryconfigure('Vista', label='Exibir')
                bar.entryconfigure('Ayuda', label='Ajuda')
                file.entryconfigure('Nuevo', label='Novo')
                file.entryconfigure('Crear', label='Criar')
                file.entryconfigure('Abrir Reciente', label='Abrir Recente')
                file.entryconfigure('Actualizar', label='Atualizar')
                file.entryconfigure('Correr', label='Executar')
                file.entryconfigure('Cercar', label='Fechar')
                file.entryconfigure('Salir', label='Sair')
                view.entryconfigure('Mostrar nombre de archivo', label='Mostrar nome do arquivo')
                view.entryconfigure('Mostrar número de líneas', label='Mostrar linhas numeradas')
                view.entryconfigure('Palabras coloreadas', label='Palavras coloridas')
                edit.entryconfigure('Modo de Lectura', label='Modo Leitura')
                edit.entryconfigure('Paleta de Colores', label='Paleta de Cores')
                ausa.entryconfigure('Siempre', label='Sempre')

            lan="Português"
            titleshow(s=False)
    if l=="Español":
        if lan!='Español':
            janela.title('Bloc de Notas')

            if lan=='English':
                bar.entryconfigure('File', label='Archivo')
                bar.entryconfigure('Edit', label='Editar')
                bar.entryconfigure('View', label='Vista')
                bar.entryconfigure('Help', label='Ayuda')
                file.entryconfigure('New', label='Nuevo')
                file.entryconfigure('Create', label='Crear')
                file.entryconfigure('Open', label='Abrir')
                file.entryconfigure('Open Recent', label='Abrir Reciente')
                file.entryconfigure('Update', label='Actualizar')
                file.entryconfigure('Save', label='Salvar')
                file.entryconfigure('Save as', label='Salvar Como')
                file.entryconfigure('Print', label='Imprimir')
                file.entryconfigure('Run', label='Correr')
                file.entryconfigure('Close', label='Cercar')
                file.entryconfigure('Quit', label='Salir')
                view.entryconfigure('Theme', label='Tema')
                view.entryconfigure('Show file name', label='Mostrar nombre de archivo')
                view.entryconfigure('Show line numbers', label='Mostrar número de líneas')
                view.entryconfigure('Colored words', label='Palabras coloreadas')
                edit.entryconfigure('Read Only', label='Modo de Lectura')
                edit.entryconfigure('Color Picker', label='Paleta de Colores')
                view.entryconfigure('Language', label='Idioma')
                help.entryconfigure('About...', label='Sobre...')
                ausa.entryconfigure('Never', label='Nunca')
                ausa.entryconfigure('1 Minute', label='1 Minuto')
                ausa.entryconfigure('5 Minutes', label='5 Minutos')
                ausa.entryconfigure('Always', label='Siempre')

            if lan=='Português':
                bar.entryconfigure('Arquivo', label='Archivo')
                bar.entryconfigure('Exibir', label='Vista')
                bar.entryconfigure('Ajuda', label='Ayuda')
                file.entryconfigure('Novo', label='Nuevo')
                file.entryconfigure('Criar', label='Crear')
                file.entryconfigure('Abrir Recente', label='Abrir Reciente')
                file.entryconfigure('Atualizar', label='Actualizar')
                file.entryconfigure('Executar', label='Correr')
                file.entryconfigure('Fechar', label='Cercar')
                file.entryconfigure('Sair', label='Salir')
                view.entryconfigure('Mostrar nome do arquivo', label='Mostrar nombre de archivo')
                view.entryconfigure('Mostrar linhas numeradas', label='Mostrar número de líneas')
                view.entryconfigure('Palavras coloridas', label='Palabras coloreadas')
                edit.entryconfigure('Modo Leitura', label='Modo de Lectura')
                edit.entryconfigure('Paleta de Cores', label='Paleta de Colores')
                ausa.entryconfigure('Sempre', label='Siempre')

            lan="Español"
            titleshow(s=False)

    savedata()

def theme(t):
    global abindex
    global thme

    if t==1:
        janela['bg']='white'
        scroll[abindex]['bg']='white'
        scroll[abindex]['fg']='black'
        lines[abindex]['bg']='snow'
        barl[abindex]['bg']='snow'
        tools['bg']='snow'
        status['bg']='snow'
        ll['bg']='snow'
        lc['bg']='snow'
        lg['bg']='snow'
        ls['bg']='snow'
    if t==2:
        janela['bg']='#111111'
        scroll[abindex]['bg']='#111111'
        scroll[abindex]['fg']='white'
        lines[abindex]['bg']='#333333'
        barl[abindex]['bg']='#333333'
        tools['bg']='#333333'
        status['bg']='#333333'
        ll['bg']='#333333'
        lc['bg']='#333333'
        lg['bg']='#333333'
        ls['bg']='#333333'

    thme=t
    savedata()

def fontc(f):
    fn.configure(family=f)
    scroll[abquant].config(font=fn)
    fnt['text']=f
    fm.add_command(label=f, command=lambda j=f:fontc(j))

def size(s):
    fn.configure(size=s)
    scroll[abquant].config(font=fn)
    siz['text']=s

def ng():
    global fn
    global b

    b=not b
    if b==True:
        fn.configure(weight="bold")
    if b==False:
        fn.configure(weight="normal")

    #scroll.tag_config(SEL_FIRST, SEL_LAST, font=fn)
    scroll[abquant].tag_add('select', SEL_FIRST, SEL_LAST)
    scroll[abquant].tag_config('select', font=fn)
    #scroll.config(font=fn)

def it():
    global fn
    global i

    i=not i
    if i==True:
        fn.configure(slant="italic")
    if i==False:
        fn.configure(slant="roman")

    scroll[abquant].config(font=fn)

def os():
    global fn
    global o

    o=not o
    if o==True:
        fn.configure(overstrike=1)
    if o==False:
        fn.configure(overstrike=0)

    scroll[abquant].config(font=fn)

def ul():
    global fn
    global u

    u=not u
    if u==True:
        fn.configure(underline=1)
    if u==False:
        fn.configure(underline=0)

    scroll[abquant].config(font=fn)

def align(al):
    global a
    print(a)

    if al==1:
        if a==2:
            scroll[abquant].tag_configure('center', justify='left')
        if a==3:
            scroll[abquant].tag_configure('right', justify='left')

        scroll[abquant].tag_add('left', 1.0, END)
    if al==2:
        if a==1:
            scroll[abquant].tag_configure('left', justify='center')
        if a==3:
            scroll[abquant].tag_configure('right', justify='center')
        
        scroll[abquant].tag_add('center', 1.0, END)
    if al==3:
        if a==1:
            scroll[abquant].tag_configure('left', justify='right')
        if a==2:
            scroll[abquant].tag_configure('center', justify='right')
        
        scroll[abquant].tag_add('right', 1.0, END)

    a=al
    print(a)

def mode(m):
    global readonly
    global tls

    if m==1:
        print("YEYE")
    if m==2:
        readonly=not readonly

        if readonly==True:
            scroll[abquant].config(state='normal')
            if tls==True:
                toolshow(False)
        if readonly==False:
            scroll[abquant].config(state='disabled')
            tools.pack_forget()
    if m==3:
        pass

def colset(c=None):
    global col
    if c==None:
        col=not col
    else:
        if c=='True': col=True
        if c=='False': col=False
    update()
    savedata()

def toolshow(c=True):
    global tls
    if c==True:
        tls=not tls

    if tls==True:
        abas.pack_forget()
        tools.pack(side='top', fill=X)
        abas.pack(side='top', fill=X)
    if tls==False:
        tools.pack_forget()

def titleshow(s=True,f=None):
    global title
    global text
    global filna
    global abindex

    if s==True:
        title=not title
    if f!=None:
        if f=="True":
            title=True
        if f=="False":
            title=False

    if title==False:
        if lan=="English":
            janela.title("Notepad")
        if lan=="Português":
            janela.title("Bloco de Notas")
        if lan=="Español":
            janela.title("Bloc de Notas")
    if title==True:
        if (text[abindex]!="Untitled"):
            n=str(OS.path.split(text[abindex])[1])
            if lan=="English":
                janela.title(n+" - Notepad")
            if lan=="Português":
                janela.title(n+" - Bloco de Notas")
            if lan=="Español":
                janela.title(n+" - Bloc de Notas")
        else:
            if lan=="English":
                janela.title("Untitled - Notepad")
            if lan=="Português":
                janela.title("Sem Título - Bloco de Notas")
            if lan=="Español":
                janela.title("Sin Titulo - Bloc de Notas")

def lineshow():
    global linumb
    linumb=not linumb

    if linumb==True:
        lines.pack(side='left', fill=Y)
    if linumb==False:
        lines.pack_forget()

def binary():
    t=scroll[abquant].get(1.0, END)
    scroll[abquant].delete('1.0', END)
    for i in t:
        inumb=ord(i)
        bnumb=bin(inumb)
        scroll[abquant].insert('1.0', bnumb)
        print(bnumb)

def autotimes(a):
    global auto
    auto=a
    savedata()

def complete(c=None):
    global auco
    if c==None:
        auco=not auco
    else:
        if c=='True': auco=True
        if c=='False': auco=False
    savedata()

def backp(c=None):
    global bckp
    if c==None:
        bckp=not bckp
    else:
        if c=='True': bckp=True
        if c=='False': bckp=False
    savedata()

def autocomplete(event,a):
    global auco
    if auco==True:
        if a==1:
            scroll[abquant].insert(INSERT,"'")
        if a==2:
            scroll[abquant].insert(INSERT,'"')
        if a==3:
            scroll[abquant].insert(INSERT,")")
        if a==4:
            scroll[abquant].insert(INSERT,"]")
        if a==5:
            scroll[abquant].insert(INSERT,"}")
        if a==6:
            scroll[abquant].insert(INSERT,">")

        scroll[abquant].mark_set(INSERT, INSERT+"-1c")

def indentation(event,i):
    global indent

    if i==1:
        print("PRESS")
        indent+=4
        print(indent)
    if i==2:
        print("Return")
        scroll[abquant].mark_set(INSERT, INSERT+'+'+str(indent)+'c')

def update(event=None):
    global filna
    global abquant
    global recent
    global text
    ind=scroll[abindex].index(INSERT)
    i=0
    t=''
    while t!='.':
        t=ind[i]
        i+=1
    li=ind[0:i-1]
    cl=ind[i:len(ind)]
    le=scroll[abindex].get(1.0, END)
    line.set("Lin: "+str(li))
    column.set("Col: "+str(cl))
    length.set("Len: "+str(len(le)-1))
    #lc['text']=(scroll.SEL_FIRST-scroll.SEL_LAST)+' selected'

    if col==True:
        if filna.endswith('.bas')==True:
            CustomText.highlight_pattern(scroll[abindex],'return ', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'print ', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'input ', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'color ', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'cls ', 'cl1', False)

            CustomText.highlight_pattern(scroll[abindex],'dim ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'as ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'if ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'else ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'then ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'do ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'for ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'loop ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'until ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'function ', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'sub ', 'cl2', False)

            CustomText.highlight_pattern(scroll[abindex],'integer ', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'string ', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'sleep', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'end', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'+', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'-', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'*', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'/', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'=', 'cl3', False)

            CustomText.highlight_pattern(scroll[abindex],'rem ', 'cl4', False)
        if filna.endswith('.html')==True:
            CustomText.highlight_pattern(scroll[abindex],'html', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'head', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'title', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'link', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'script', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'style', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'meta', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'body', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'div', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'span', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'button', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'input', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'img', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'iframe', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'h1', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'h2', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'h3', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'h4', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'h5', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'p', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'br', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'li', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'ul', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'table', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'tr', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'th', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'td', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'form', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'submit', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'fieldset', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'legend', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'select', 'cl1', True)
            CustomText.highlight_pattern(scroll[abindex],'option', 'cl1', True)

            CustomText.highlight_pattern(scroll[abindex],'id', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'name', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'class', 'cl2')


            CustomText.highlight_pattern(scroll[abindex],'href', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'src', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'alt', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'type', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'onClick', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'width', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'height', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'placeholder', 'cl2')
            CustomText.highlight_pattern(scroll[abindex],'value', 'cl2')
        if filna.endswith('.py')==True:
            CustomText.highlight_pattern(scroll[abindex],'print', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'input', 'cl1', False)
            CustomText.highlight_pattern(scroll[abindex],'len', 'cl1', False)

            CustomText.highlight_pattern(scroll[abindex],'global', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'import', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'while', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'for', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'in', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'if', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'elif', 'cl2', False)
            CustomText.highlight_pattern(scroll[abindex],'else', 'cl2', False)

            CustomText.highlight_pattern(scroll[abindex],'True', 'cl3', False)
            CustomText.highlight_pattern(scroll[abindex],'False', 'cl3', False)

            CustomText.highlight_pattern(scroll[abindex],'def', 'cl4', False)

def savedata():
    global recent
    global thme
    global lan
    global auto
    global auco
    global col
    
    fl=open('NotepadData.db','w')
    fl.write('l'+str(lan)+'\n')
    fl.write('t'+str(thme)+'\n')
    fl.write('a'+str(auto)+'\n')
    fl.write('c'+str(auco)+'\n')
    fl.write('s'+str(title)+'\n')
    fl.write('w'+str(col)+'\n')
    fl.write('b'+str(bckp)+'\n')
    for i in recent:
        if i.endswith('\n')==False:
            fl.write(i+'\n')
        else:
            fl.write(i)
    fl.write('END')
    fl.close()

#Janela
janela=Tk()
janela.title('Notepad')
janela.geometry("800x400+300+300")
# janela.iconbitmap(default='pencil.ico')
fn=Font(family="Consolas", size=12, weight="normal")

#Barras
bar=Menu(janela)
janela.config(menu=bar)
tools=Label(janela)
abas=ttk.Notebook(janela)
status=Frame(janela)

#Abas
ab=[]
ab.append(ttk.Frame(abas))
abas.add(ab[0], text='Text')
ab[abquant].rowconfigure(0, weight=300)
ab[abquant].columnconfigure(1, weight=300)

#ScrolledText
lines=[]
scroll=[]
barx=[]
bary=[]
barl=[]
lines.append(Canvas(ab[abquant], width=20))
scroll.append(Text(ab[abquant], width=1000, height=3000, borderwidth=0, wrap=None))
barx.append(Scrollbar(ab[abquant], orient='horizontal', command=scroll[abquant].xview, cursor='arrow'))
bary.append(Scrollbar(ab[abquant], orient='vertical', command=scroll[abquant].yview, cursor='arrow'))
scroll[abquant].config(font=fn, xscrollcommand=barx[abquant].set, yscrollcommand=bary[abquant].set)
barl.append(Label(ab[abquant]))
i=0
while i<1000:
    lines[abquant].create_text(1,i*19,text=i,anchor=N+W)
    i+=1

#File Menu
file=Menu(bar, tearoff=0)
hist=Menu(file, tearoff=0)
bar.add_cascade(label='File', menu=file)
file.add_command(label='New', command=new)
file.add_command(label='Create', command=create)
file.add_command(label='Open', command=opn)
file.add_cascade(label='Open Recent', menu=hist)
file.add_cascade(label='Update', command=upopn)
file.add_command(label='Save', command=sav)
file.add_command(label='Save as', command=savas)
file.add_separator()
file.add_command(label='Print', command=printer)
file.add_command(label='Run', command=lambda:run().start())
file.add_separator()
file.add_command(label='Close', command=clo)
file.add_command(label='Quit', command=qut)

#Edit Menu
aus=StringVar()
edit=Menu(bar, tearoff=0)
ausa=Menu(edit, tearoff=0)
bar.add_cascade(label='Edit', menu=edit)
edit.add_checkbutton(label='Read Only', command=lambda:mode(2))
edit.add_checkbutton(label='Color Picker', command=colorpicker)
edit.add_checkbutton(label='Auto Complete', command=complete)
edit.add_checkbutton(label='Backup Files', command=backp)
edit.add_cascade(label='Auto-Save', menu=ausa)
ausa.add_radiobutton(label='Never', command=lambda:autotimes(0), variable=aus, value=1)
ausa.add_radiobutton(label='1 Minute', command=lambda:autotimes(60), variable=aus, value=2)
ausa.add_radiobutton(label='5 Minutes', command=lambda:autotimes(300), variable=aus, value=3)
ausa.add_radiobutton(label='Always', command=lambda:autotimes(1), variable=aus, value=4)

#View Menu
view=Menu(bar, tearoff=0)
bar.add_cascade(label='View', menu=view)
language=Menu(view, tearoff=0)
them=Menu(view, tearoff=0)
view.add_cascade(label='Language', menu=language)
view.add_cascade(label='Theme', menu=them)
view.add_checkbutton(label='Tools', command=toolshow)
view.add_checkbutton(label='Show file name', command=titleshow)
view.add_checkbutton(label='Show line numbers', command=lineshow)
view.add_checkbutton(label='Colored words', command=colset)
view.add_command(label='Binary', command=binary)

#View-Language
language.add_command(label='English', command=lambda:lang("English"))
language.add_command(label='Português', command=lambda:lang("Português"))
language.add_command(label='Español', command=lambda:lang("Español"))

#View-Theme
them.add_command(label='Light', command=lambda:theme(1))
them.add_command(label='Dark', command=lambda:theme(2))

#Help Menu
help=Menu(bar, tearoff=0)
bar.add_cascade(label='Help', menu=help)
help.add_command(label='About...', command=abo)
help.add_command(label='How to use', command=lambda:OS.system("start NotepadHelp.rtf"))
help.add_command(label='Twitter', command=lambda:webbrowser.open_new('https://twitter.com/KaiXtr'))
help.add_command(label='Reddit', command=lambda:webbrowser.open_new('https://www.reddit.com/user/KaiXtr'))


#Tools
fnt=Menubutton(tools, relief="groove")
fm=Menu(fnt, tearoff=0)
fnt["menu"]=fm

fonts=[]
for f in OS.listdir('/usr/share/fonts'):
    if f.endswith(".ttf")==True:
        f=f[0:-4]
        f=f.capitalize()
        fonts.append(f)
        fn=Font(family=str(f))
        val=fn
        fm.add_command(label=f, command=lambda j=f:fontc(j))
if len(fonts) > 0:
    fnt["text"]=fonts[0]

siz=Menubutton(tools, text=10, relief="groove")
sm=Menu(siz, tearoff=0)
siz["menu"]=sm
while i<100:
    i+=1
    sm.add_command(label=i, command=lambda j=i:size(j))
ngicon=PhotoImage(file='Bold.png')
neg=Button(tools, text="N", command=ng, image=ngicon, relief="groove", width=20, height=20)
ita=Button(tools, text="/", command=it, relief="groove")
ovs=Button(tools, text="-", command=os, relief="groove")
unl=Button(tools, text="_", command=ul, relief="groove")

lal=Button(tools, text="<", command=lambda:align(1), relief="groove")
cal=Button(tools, text="^", command=lambda:align(2), relief="groove")
ral=Button(tools, text=">", command=lambda:align(3), relief="groove")

#Status
line=StringVar()
column=StringVar()
length=StringVar()
ll=Label(status, textvariable=line)
lc=Label(status, textvariable=column)
lg=Label(status, textvariable=length)
lc=Label(status)
ls=Label(status)

#Posições
#tools.pack(side='top', fill=X)
abas.pack(side='top', fill=BOTH, expand=1)
status.pack(side='bottom', fill=X)

fnt.pack(side='left')
siz.pack(side='left')
neg.pack(side='left')
ita.pack(side='left')
ovs.pack(side='left')
unl.pack(side='left')

lal.pack(side='right')
cal.pack(side='right')
ral.pack(side='right')

lines[abquant].grid(row=0, column=0, sticky=N+S)
scroll[abquant].grid(row=0, column=1, sticky=N+S+W+E)
barx[abquant].grid(row=2, column=1, sticky=W+E)
bary[abquant].grid(row=0, column=2, sticky=N+S)
barl[abquant].grid(row=2, column=2, sticky=N+S+W+E)

ll.pack(side='left')
lc.pack(side='left')
lg.pack(side='left')
lc.pack(side='left')
ls.pack(side='left')

#CARREGAR DADOS
fileopen=open('NotepadData.db','r')
while True:
    n=str(fileopen.readline())
    if n[0]=='l':
        lang(n[1:-1])
    elif n[0]=='t':
        theme(int(n[1:-1]))
    elif n[0]=='a':
        autotimes(int(n[1:-1]))
    elif n[0]=='c':
        complete(n[1:-1])
    elif n[0]=='s':
        titleshow(False,n[1:-1])
    elif n[0]=='w':
        colset(n[1:-1])
    elif n[0]=='b':
        backp(n[1:-1])
    elif n=='END':
        break
    else:
        recent.append(n[0:-1])
        if recent[ind]!="":
            dt=str(OS.path.split(recent[ind])[1])
            if dt.endswith('\n')==True:
                dt=dt[0:-1]
            hist.add_command(label=dt, command=lambda val=ind:opnrec(val))
        ind+=1
fileopen.close()
savedata()

scroll[abquant].tag_configure('cl1', foreground='blue')
scroll[abquant].tag_configure('cl2', foreground='orange')
scroll[abquant].tag_configure('cl3', foreground='red')
scroll[abquant].tag_configure('cl4', foreground='green')

abas.bind('<<NotebookTabChanged>>', tabch)
janela.bind('<Key>', update)
janela.bind('<Tab>', lambda event,i=1:indentation(event, i))
janela.bind('<Return>', lambda event,i=2:indentation(event, i))
janela.bind("'", lambda event, a=1:autocomplete(event, a))
janela.bind('"', lambda event, a=2:autocomplete(event, a))
janela.bind('(', lambda event, a=3:autocomplete(event, a))
janela.bind('[', lambda event, a=4:autocomplete(event, a))
janela.bind('{', lambda event, a=5:autocomplete(event, a))
janela.bind('<less>', lambda event, a=6:autocomplete(event, a))

janela.bind('<Control-n>', lambda event=None:new())
janela.bind('<Control-Shift-n>', lambda event=None:create())
janela.bind('<Control-o>', lambda event=None:opn())
janela.bind('<Control-s>', lambda event=None:sav())
janela.bind('<Control-Shift-s>', lambda event=None:run().start())
janela.bind('<Control-b>', lambda event=None:run())
scroll[abindex].bind('<Button-1>', update)

if auto>0:
    autosave().start()
janela.protocol("WM_DELETE_WINDOW", qut)
janela.mainloop()