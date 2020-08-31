import urllib as url
import random as rand
import requests as req
import webbrowser as web
from bs4 import BeautifulSoup as BS

#custom library that just has useragents in
from UserAgent import UserAgents as UA

#this function will generate 6 chars which represents an image in the prnt.sc database
#and can be viewed in the browser
def generateUrl():
    e = ''
    o = 0    
    for o in range(6):
        urlchars = '123456789abcdefghijklmnop'
        e += rand.choice(urlchars)
    url = f'https://prnt.sc/{e}'
    imgurl = getimg(url)
    print(f'Url generated: {url}')

    #will open the url generated
    web.open(url)

#this will grab the images src .jpg/.png
def getimg(url):
    headers = {"User-Agent": UA.getRandUA()}
    r = req.get(url, headers=headers)
    html = r.content
    soup = BS(html, 'html.parser')
    imgurl = soup.find('img', {'class': 'no-click screenshot-image'})['src']
    return imgurl

#simple loop to generate 10 urls
#change the range to however many you want to generate.
i = 0
for i in range(10):
    generateUrl()

