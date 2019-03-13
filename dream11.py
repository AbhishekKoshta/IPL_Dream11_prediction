import time
start_time = time.time()
import pandas as pd
# data = pd.read_csv('basemodel.csv')
data = pd.read_csv('deliveries.csv')

ldf = pd.DataFrame()
Match_id = []
Name = []
Runs = []; 	# No. of runs scored by a batsman in a match
boPld = []  # No. of balls played by a batsman in a match
chauke =[] 	# No. of fours a batsman hit in a match
chhakke = []  # No. of sixes
catches = []
runout = []  # How many runouts a player have got
strkrate = []  # Strike rate of a batsman in a match
d11sc = []
## Get all the players who batted in a match 
print (data["batsman"].unique())
print ("Please choose a player from the above array ")

# For a single match
# if data['match_id'][i]==1:
# Runs scored by a player

for mid in range(1,637):
	PlayerName = "S Dhawan"
	# mid = 1
	print ("Player Choosen: ", PlayerName)
	# PlayerName = input("\nEnter the name of the player ")
	print ("Wait...We are generating player's stats for match", mid)

	## Batting score
	ballsPlayed = data[(data["batsman"]== PlayerName) &(data['match_id']==mid)]["batsman_runs"].count()
	if ballsPlayed == 0:
		continue
	RunPlayer = data[(data["batsman"]== PlayerName) &(data['match_id']==mid)]["batsman_runs"].sum()
	SR = RunPlayer/ballsPlayed
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

	## Dream 11 score
	dr11Score = RunPlayer*0.5+Four_byPlayer*0.5+Six_byPlayer+bonusScore + fieldScore + penaltyScore
	print ("batsman:",PlayerName,"Runs",RunPlayer,"Balls played" ,ballsPlayed,"4s",Four_byPlayer, "6s",Six_byPlayer,"Strike Rate",SR,"\nDream11 Score", dr11Score)



	# Appending all the data to lists to finally give it to panda and write on csv/excel file
	Match_id.append(mid)
	Name.append(PlayerName)
	Runs.append(RunPlayer)
	boPld.append(ballsPlayed)
	chauke.append(Four_byPlayer) 
	chhakke.append(Six_byPlayer)
	strkrate.append((int(SR*100)))
	catches.append(cfieldScore) 
	runout.append(rfieldScore)
	d11sc.append(dr11Score)


ldf["Sr_No"] = [i for i in range(len(Match_id))]
ldf["MatchID"] = Match_id
ldf["Name"] = Name
ldf["Runs"] = Runs
ldf["Balls"] = boPld
ldf["4s"] = chauke
ldf["6s"] = chhakke
ldf["Strike_Rate"] = strkrate

ldf["Catches"] = catches
ldf["Run_Out"] = runout
ldf["Dream11Score"] = d11sc




ldf.to_csv("{}.csv".format(PlayerName),index=False)
print ("Time taken in the process", time.time()-start_time)