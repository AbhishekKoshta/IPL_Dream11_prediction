import pandas as pd

data = pd.read_csv('basemodel.csv')

## Get all the players who batted in a match 
print (data["batsman"].unique())
print ("Please choose a player from the above array ")

# For a single match
for i in range(len(data)):
# for i in range(len(data)):
	if data['match_id'][i]==1:
		# Runs scored by a player
		PlayerName = "CH Gayle"
		print ("Player Choosen: ", PlayerName)
		# PlayerName = input("\nEnter the name of the player ")
		print ("Wait...We are generating player's stats")
		RunPlayer = data[data["batsman"]== PlayerName]["batsman_runs"].sum()
		Four_byPlayer = data[(data["batsman"]== PlayerName) & (data["batsman_runs"]== 4)]["batsman_runs"].count()
		Six_byPlayer = data[(data["batsman"]== PlayerName) & (data["batsman_runs"]== 6)]["batsman_runs"].count()

		if RunPlayer >= 100:
			bonusScore = 8
		elif RunPlayer >=50:
			bonusScore = 4
		else:
			bonusScore = 0
			
		## Fielding Score
		cfieldScore = data[(data["fielder"]==PlayerName) & (data["dismissal_kind"]=="caught")]['dismissal_kind'].count()
		rfieldScore = data[(data["fielder"]==PlayerName) & (data["dismissal_kind"]=="run out")]['dismissal_kind'].count()

		fieldScore = cfieldScore*4+rfieldScore*4


		## Bowling score
		bfieldScore = data[(data["bowler"]==PlayerName) & (data["dismissal_kind"]=="bowled")]['dismissal_kind'].count()


		dr11Score = RunPlayer*0.5+Four_byPlayer*0.5+Six_byPlayer+bonusScore + fieldScore

print ("batsman",PlayerName,Four_byPlayer,"4s",Six_byPlayer,"6s","Dream11 Score", dr11Score)

