from urllib.request import *
import webbrowser
import re


url='http://teition.com/using-pythons-webbrowser-package-to-open-a-website-url/'
doc=urlopen(url)
sou=doc.read()
doc.close()
print(re.search('html',str(sou),re.M|re.I))


#webbrowser.open_new(url)