import csv
import requests 
from BeautifulSoup import BeautifulSoup

url = "http://www.espn.com/college-football/rankings"
response = requests.get(url)
html = response.content 

soup = BeautifulSoup(html)

table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr'):

    list_of_cells = []

    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')

        text = cell.text.replace('&mdash;', '')

        list_of_cells.append(text)

    list_of_rows.append(list_of_cells)


outfile = open("./rank.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Rank", "School", "Record ", "Points", "Trend"])
writer.writerows(list_of_rows)