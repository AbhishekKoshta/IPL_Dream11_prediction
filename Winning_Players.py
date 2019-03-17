import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

AllTeam = ["Chennai Super Kings","Royal Challengers Bangalore"]
#Match_between 
team1=AllTeam[0]
team2=AllTeam[1]

# Get the players of both the team on a list
team1 = pd.read_csv("J:\\JQM\\IPL_Dream11_prediction\\Teams_2019\\{}_2019e.csv".format(team1))["Players"]
team2 = pd.read_csv("J:\\JQM\\IPL_Dream11_prediction\\Teams_2019\\{}_2019e.csv".format(team2))["Players"]
players = team1.append(team2)

dt = pd.read_csv("FinalPlayerRating.csv")

# tm = dt[dt["Players"]
dream11Scores = []
wdream11Scores = []
Notindb = []
# for i in range(len(players)):
for i in players:

	try:
		score = dt[dt["Players"]==i]["Avg_Total"].values[0]
		weighted_score = dt[dt["Players"]==i]["wAvg_Total"].values[0]
		# print (i,score)
	except:
		# print ("Player {} is not matching in our database".format(i))
		Notindb.append(i)
		continue
	dream11Scores.append((score,i))
	wdream11Scores.append((weighted_score,i))

dream11Scores.sort(reverse=True)
wdream11Scores.sort(reverse=True)
print ("\n===========================Dream11 team based on average dream11 score===========================")
print (dream11Scores[:11])
print ("\n===========================Dream11 team based on weighted average dream11 score===========================")
print (wdream11Scores[:11])

print ("\n=========================================")
print ("Players not being considered")
print (Notindb)
# print (dream11Scores.sort())
# print (np.concatenate(team1,team2),axis=1)