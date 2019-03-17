import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

AllTeam = ["Chennai Super Kings","Royal Challengers Bangalore"]
Team = AllTeam[1]
df = pd.read_csv("J:\\JQM\\IPL_Dream11_prediction\\Teams_2019\\{}.csv".format(Team))["Players"].values
df1 = pd.read_csv("AllPlayers.csv",encoding="ISO-8859-1")["Players"]

dt = pd.DataFrame()
ActPl = []
MatchPl = []
for i in df:
	match = process.extractOne(i,df1.values)
	print (i,match)
	ActPl.append(i)
	MatchPl.append(match[0])

dt["Players"] = MatchPl
dt["Actual Name"] = ActPl
dt.to_csv("J:\\JQM\\IPL_Dream11_prediction\\Teams_2019\\{}_2019.csv".format(Team))
