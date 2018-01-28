import urllib
import re
import json

htmltext = urllib.urlopen("http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/celtics_roster.json")

data = json.load(htmltext)


for i in range(0):
	x = len(data['t']['pl'])
	print(x)


