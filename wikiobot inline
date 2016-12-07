import sys
import telepot
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
import sys
import time
from bs4 import BeautifulSoup
import requests
import re

def on_inline_query(msg):
	query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
	print ('Inline Query:', query_id, from_id, query_string)
	#print (type(query_string))
	if True:
		#p = re.sub(r'[?|$|.|!]',r'',msg['text'])
		url = 'https://www.google.co.in/search?q=define%20' + query_string + '#cns=1'
		response = requests.get(url, headers={"user-agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0"})
		html = response.content
		final_soup = BeautifulSoup(html, 'html.parser')
		everyThing = final_soup.select("div._Jig")
		s = ""
		for line in everyThing:
			s = s + ("-" + line.text)
			#s = s + "\n"
			break
	print (s)
	articles = [InlineQueryResultArticle(id='abc',title='tu pagal hai',input_message_content=InputTextMessageContent(message_text=s))]
	#articles = [InlineQueryResultArticle(id='abc',title='ABC',input_message_content=InputTextMessageContent(message_text=s))]
	
	bot.answerInlineQuery(query_id, articles)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot('307264511:AAG1GnmAkNZ6D7pjhhypAeIkYSdAuVrPNAs')
bot.message_loop({'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result},
                 run_forever='Listening ...')
