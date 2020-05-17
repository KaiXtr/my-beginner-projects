import tweepy
import urllib
from bs4 import BeautifulSoup

'''auth = tweepy.OAuthHandler(usertok,usersecret)
auth.set_access_token(accestok,acesssecret)
api = tweepy.API(auth)'''

page=urllib.request.urlopen('https://www.apolo11.com/asteroides.php')
content=BeautifulSoup(page.read())
fonts=content.findAll('div')
for font in fonts:
	if "class" in font:
		if (font["class"]=="f20 red bold"):
			meteordata=content.font

infotweet='o próximo meteoro virá em '+str(meteordata)+'n/https://www.apolo11.com/asteroides.php'
print(infotweet)

'''api.update_status(infotweet)

for tweet in api.search('#vemmeteoro', lang=):
    api.retweet(tweet.id)

for tweet in api.search('@meteoro_bot', lang=):
    api.update_status(infotweet)

for tweet in api.search('vem meteoro', lang=):
    replyurl=tweet.url
    #reply=api.get_status(replyurl)
    api.update_status(infotweet, in_reply_to_status_id=replyurl)
    
img=[]
for file in os.pathdir('/sdcard/Meteoro Bot/'):
	if file.endswith('.jpg'):img.append(file)
	
