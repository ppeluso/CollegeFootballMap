import csv
import requests
from BeautifulSoup import BeautifulSoup
import pandas as pd
import numpy as np
import unicodedata
from sqlalchemy import *
import sqlite3
import geocoder
from score import tosqlfile

url = "https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_stadiums"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find("table", {'class': "wikitable sortable"})
city = []
state = []
name = []
cap = []
team_name = []
for row in table.findAll("tr"):
	cells = row.findAll('td')
	if len(cells) != 0:
		name.append(cells[1].find(text = True))
		city.append(cells[2].find(text = True))
		state.append(cells[3].find(text = True))
		team_name.append(cells[4].find(text = True))
		cap.append(cells[6].find(text = True))

stadium = pd.DataFrame({"Stadium": np.array(name), "City": np.array(city), 
	                  "State": np.array(state), "Team": np.array(team_name), "Capacity": np.array(cap)})

db = create_engine('sqlite:///./score/score.db')

#stadium.to_sql('stadium', db,'sqlite',if_exists='replace')
# hold = []
# new = pd.read_sql("Week10", db)
# for i in range(len(new["Home"])):
# 	for j in range(len(stadium["Team"])):
# 		if new["Home"][i] == stadium["Team"][j]:
# 			hold.append(stadium["Stadium"][i])
# 			break
# 	else:
# 		hold.append("NaN")
lat =[]
lng = []
for i in range(len(stadium['Stadium'])):
	string = stadium['City'][i]+ ',' + stadium['State'][i]
	loc = geocoder.google(string)
	print(loc.latlng)
	if loc.latlng:
		lat.append(loc.latlng[0])
		lng.append(loc.latlng[1]) 
	else:
		lat.append("NaN")
		lng.append("NaN")
stadium = pd.DataFrame({"Stadium": np.array(name), "City": np.array(city), 
	                  "State": np.array(state), "Team": np.array(team_name), "Capacity": np.array(cap), "Lat": np.array(lat), "lng": np.array(lng)})

stadium.to_sql('stadium', db,'sqlite',if_exists='replace')

# conn = sqlite3.connect("./score/socre.db")
# c = conn.cursor()
# c.execute("alter table {table}")
