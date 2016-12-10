import json
import urllib2

url = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=xgfW29gz4Ig&fields=items(snippet(topLevelComment(snippet(authorDisplayName%2CtextDisplay))))&key=AIzaSyAlkXC-_pd5n1tylj8zr7NSK9o1VXzhTGY'

f = urllib2.urlopen(url)
data = json.load(f)
 file = open('new.txt','w')
for item in data['items']:
	u = (item['snippet']['topLevelComment']['snippet']['authorDisplayName'])
    s = (item['snippet']['topLevelComment']['snippet']['textDisplay'])
    file.write(u.encode('ascii','ignore'))
    file.write('\n')
    file.write(s.encode('ascii','ignore'))
    file.write('\n')
    file.write('\n')
file.close()
