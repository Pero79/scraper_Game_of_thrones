from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.title.string + "\n"
file = open("GoTviewers.txt", "w+")
file.write("All episode wievs of GoT: " + "\n")

wikitable = soup.findAll("table", attrs={"class": "wikitable"})

total_sum_views = 0
seasons_views_sum = 0

for tr in wikitable[1].findAll("tr"):
    for td in tr.findAll("td"):
        table_data = td.string
        if table_data is not None and table_data != "N/A":
            one_season_wievs = str(table_data)
            seasons_views_sum += float(table_data)
            file.write(one_season_wievs + "\n")


total_sum_views = str(seasons_views_sum)
print "All wiews GoT: " + total_sum_views
file.write("All wievs of GoT: ")
file.write(total_sum_views)

file.close()