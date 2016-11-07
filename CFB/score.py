import csv
import requests
from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import unicodedata

url = "http://www.ncaa.com/scoreboard/football/fbs/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
data = soup.findAll("div", {'class': "game-contents"})

team = []
# Finds all teams 
for i in data:
    find_team = i.findAll('a')
    for y in find_team:
        z = y
        for q in z:
        	team.append(q)

team = [x for x in team if x != "GameCenter &raquo;" and x != 
        "Video Highlight &raquo;"]

# finds final score of each game
info = []

for i in data:
    find_score = i.findAll("td", {"class": "final score"})
	
    for x in find_score:
        info.append(x.text)

final = []

for x in info:
    final.append(x)

####### scrapes for week of scores #########

date = soup.find("hgroup", {"class": "visible"}).h4.contents

away = []
home = []
away_score = []
home_score = []

for i in range(len(team)):
    if i%2 == 0:
        away.append(team[i])
        away_score.append(final[i])
    else:
    	if team[i] == "Northern Ill.":
    		team[i] = "NIU"
    	elif team[i] == "Miami (Ohio)":
    		team[i] = "Miami (OH)"
    	elif team[i] == "Mississippi St.":
    		team[i] = 'Mississippi State'
    	elif team[i] == 'Washington St.':
    		team[i] = 'Washington State'
    	elif team[i] == 'Army West Point':
    		team[i] = "Army"
    	elif team[i] == 'Miami (Fla.)':
    		team[i] = "Miami"  
    	elif team[i] == 'Middle Tenn.':
    		team[i] = "Middle Tennessee"
    	elif team[i] == 'La.-Monroe':
    		team[i] = "Louisiana-Monroe"  
    	elif team[i] == 'La.-Lafayette':
    		team[i] = "Louisiana-Lafayette"
    	elif team[i] == 'Western Ky.':
    		team[i] = "Western Kentucky"
    	elif team[i] == 'USC':
    		team[i] = "Southern California"     		    		  		    		  		
        home.append(team[i])
        home_score.append(final[i])

date = str(date[0])
date = date.replace(" ", '')
file = "./score/{week}.csv".format(week = date)
tosqlfile = "{week}".format(week = date)
away = np.array(away)
home = np.array(home)
away_score = np.array(away_score)
home_score = np.array(home_score)

# df = pd.DataFrame({"Away " : away, "away_score" : away_score, "Home": home, "home_score": home_score})

# old = pd.read_csv(file)
# df.to_csv(file, index=False)
# new = pd.read_csv(file)
# print(pd.DataFrame.equals(new,old))


date = soup.findAll('div', {'class': ['game-status pre ', "game-status final ", 
	                "game-status postponed ", "game-status live "]})

time = []
for i in date:
	time.append(i.text)

time = np.array(time)
