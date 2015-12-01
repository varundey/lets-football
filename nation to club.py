import json
file = '/home/varun/Desktop/lets-football/crawler/nation_data.txt'
dic=json.load(open(file))

print "Enter country"
print id
url = "http://www.national-football-teams.com/country/"+str(dic[raw_input()])+"/2015/Italy.html"
import requests
from bs4 import BeautifulSoup as b
#url = "http://www.national-football-teams.com/country/"+str(174)+"/2015/Italy.html"
soup  = b(requests.get(url).content,"lxml")

club= []

table= soup.find("table",{"class":"sortable"}).find('tbody').findAll('tr')
for per_tr in table:
	td = per_tr.findAll('td')
	for i in range(5):
		if i==3:
			continue
		print td[i].text.strip()	
		club.append(td[4].text.strip().encode('ascii', 'ignore'))
	print '---------------------------'
	
total_clubs = len(club)

dic={x:club.count(x) for x in club}
#print dic
print "Below are the team club stats in percent"
for i in dic:
	print i+" \t\t\t| %.3f"%((100.000*dic[i])/total_clubs)+"\t\t|"+str(dic[i])
