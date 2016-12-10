import telepot
import sys
import time
from bs4 import BeautifulSoup
import requests
import re

bot = telepot.Bot('Bot Key')
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)
	
	if content_type == 'text' and msg['text'].endswith("?") == True:
		#p = re.sub(r'[?|$|.|!]',r'',msg['text'])
		url = 'https://www.google.co.in/search?q=define%20' + msg['text'] + '#cns=1'
		response = requests.get(url, headers={"user-agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0"})
		html = response.content
		final_soup = BeautifulSoup(html, 'html.parser')
		everyThing = final_soup.select("div._Jig")
		s = ""
		for line in everyThing:
			s = s + ("-" + line.text)
			s = s + "\n"
			break
		if len(s)>400:
			
		bot.sendMessage(chat_id, s)

#TOKEN = sys.argv[1]


bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
