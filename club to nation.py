import requests
from bs4 import BeautifulSoup as b
i=1
dic={}
while True:
	
	soup = b(requests.get("http://www.national-football-teams.com/club/"+str(i)+"/2015_1/Real_Madrid.html").content,"lxml")
	
	club = soup.findAll("div",{"class":"span6"})[2].find('h1')
	
	if club:
		if club.find('small'):
			club.find('small').replaceWith('')
		
#		print club.text.encode('ascii','ignore')
		dic.update({club.text.encode('ascii','ignore'):i})
		print dic
		i+=1
