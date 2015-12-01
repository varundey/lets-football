from bs4 import BeautifulSoup as b
import requests
import json
file = open('nation_data.txt','a')
i = 1

dic = {}
DIC={}
l = ["country",'id']

while True:
	country = b(requests.get("http://www.national-football-teams.com/country/"+str(i)+"/2015/Italy.html").content,"lxml").findAll("div",{"class":"span6"})[2].find('h1')

	if country:
		if country.find('small'):
			country.find('small').replaceWith ('')

		dic.update({country.text.encode('utf-8'):i})

		print dic
		i+=1
	else:
		print 546666666666666666666666666666666666666665
		break

json.dump(dic,file)
