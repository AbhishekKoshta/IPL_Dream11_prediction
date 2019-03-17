import pandas as pd
df = pd.read_csv("deliveries.csv")
AllPlayers = df["batsman"].unique()
pd.DataFrame({"Players":AllPlayers}).to_csv("AllPlayers.csv")

bat = df["batsman"].unique().tolist()
print (len(bat))
bat.append(df["bowler"].unique().tolist())
# print (bat, bowl)
print (type(bat), len(bat))
# creatingTeam = 
# for i in range(len(df)):
# for Team in team:
# 	batsman = df[df["batting_team"]==Team]["batsman"].unique() 
# 	print (Team, batsman)
# 	pd.DataFrame({"Players":batsman}).to_csv("{}.csv".format(Team))	
	# team = df["batting_team"]
	# teamPlayer = 

