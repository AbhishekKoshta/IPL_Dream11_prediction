import pandas as pd
data = pd.read_csv('basemodel.csv')
ldf = pd.DataFrame()
Match_id = []
Name = []
Runs = []
## Get all the players who batted in a match 
print (data["batsman"].unique())
print ("Please choose a player from the above array ")

# For a single match
# if data['match_id'][i]==1:
# Runs scored by a player
PlayerName = "S Dhawan"
mid = 1
print ("Player Choosen: ", PlayerName)
# PlayerName = input("\nEnter the name of the player ")
print ("Wait...We are generating player's stats")


## Batting score
RunPlayer = data[(data["batsman"]== PlayerName) &(data['match_id']==mid)]["batsman_runs"].sum()
bowlsPlayed = data[(data["batsman"]== PlayerName) &(data['match_id']==mid)]["batsman_runs"].count()
SR = RunPlayer/bowlsPlayed
Four_byPlayer = data[(data["batsman"]== PlayerName)& (data['match_id']==mid) & (data["batsman_runs"]== 4)]["batsman_runs"].count()
Six_byPlayer = data[(data["batsman"]== PlayerName)& (data['match_id']==mid) & (data["batsman_runs"]== 6)]["batsman_runs"].count()

if RunPlayer >= 100:
	bonusScore = 8
elif RunPlayer >=50:
	bonusScore = 4
else:
	bonusScore = 0

if SR <= 0.5:
	penaltyScore = -3
elif SR > 0.5 and SR <=0.599:
	penaltyScore = -2
elif SR>=0.6 and SR <= 0.7:
	penaltyScore = -1
else:
	penaltyScore = 0
		
## Fielding Score
cfieldScore = data[(data["fielder"]==PlayerName) & (data['match_id']==mid) & (data["dismissal_kind"]=="caught")]['dismissal_kind'].count()
rfieldScore = data[(data["fielder"]==PlayerName) & (data['match_id']==mid) & (data["dismissal_kind"]=="run out")]['dismissal_kind'].count()

fieldScore = cfieldScore*4+rfieldScore*4


## Bowling score
bfieldScore = data[(data["bowler"]==PlayerName) & (data["dismissal_kind"]=="bowled")]['dismissal_kind'].count()





dr11Score = RunPlayer*0.5+Four_byPlayer*0.5+Six_byPlayer+bonusScore + fieldScore + penaltyScore
print ("batsman:",PlayerName,"Runs",RunPlayer,"Balls played" ,bowlsPlayed,"4s",Four_byPlayer, "6s",Six_byPlayer,"Strike Rate",SR,"\nDream11 Score", dr11Score)

Match_id.append(match_id)
Name.append(PlayerName)
Runs.append(RunPlayer)

ldf["MatchID"] = Match_id
ldf["Name"] = Name
ldf["Runs"] = Runs

ldf.to_csv("Results.csv")
