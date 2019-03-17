import pandas as pd
import numpy as np
data = pd.read_csv('deliveries.csv')

## Get all the players who batted in a match
print (data["batsman"].unique())
print ("Please choose a player from the above array ")

allBatsman = data["batsman"].unique()
# For a single match

dt=pd.DataFrame()
lno_of_matches=[]
player=[]

lavg_asBataman=[]
lavg_asBowler=[]
lavg_asFielder=[]
lavg_d11sc=[]
lstd_asBataman=[]
lstd_asBowler=[]
lstd_asFielder=[]
lstd_d11sc=[]

lwavg_asBataman=[]
lwavg_asBowler=[]
lwavg_asFielder=[]
lwavg_d11sc=[]
lwstd_asBataman=[]
lwstd_asBowler=[]
lwstd_asFielder=[]
lwstd_d11sc=[]

for PlayerName in allBatsman:

	try:
		df = pd.read_csv("{}.csv".format(PlayerName))
	except:
		continue

	no_of_matches = len(df)
	# print (df.head())
	avg_asBataman = df["asBataman"].mean()
	avg_asBowler = df["asBowler"].mean()
	avg_asFielder = df["asFielder"].mean()
	avg_d11sc = df["Dream11Score"].mean()

	std_asBataman = df["asBataman"].std()
	std_asBowler = df["asBowler"].std()
	std_asFielder = df["asFielder"].std()
	std_d11sc = df["Dream11Score"].std()


	## Weighted average	

	# for i in range(no_of_matches):
	# 	print (df["asBataman"][i])

	wavg_asBataman = np.mean([i*df["asBataman"][i]/no_of_matches for i in range(no_of_matches)])
	wavg_asBowler = np.mean([i*df["asBowler"][i]/no_of_matches for i in range(no_of_matches)])
	wavg_asFielder = np.mean([i*df["asFielder"][i]/no_of_matches for i in range(no_of_matches)])
	wavg_d11sc = np.mean([i*df["Dream11Score"][i]/no_of_matches for i in range(no_of_matches)])

	# print ("=================================================")
	# print ("Weighted average for ", PlayerName)
	# print (wavg_asBataman,wavg_asBowler)
	# print ("=================================================")
	wstd_asBataman = np.std([i*df["asBataman"][i]/no_of_matches for i in range(no_of_matches)])
	wstd_asBowler = np.std([i*df["asBowler"][i]/no_of_matches for i in range(no_of_matches)])
	wstd_asFielder = np.std([i*df["asFielder"][i]/no_of_matches for i in range(no_of_matches)])
	wstd_d11sc = np.std([i*df["Dream11Score"][i]/no_of_matches for i in range(no_of_matches)])

	lno_of_matches.append(no_of_matches)

	lavg_asBataman.append(avg_asBataman)
	lavg_asBowler.append(avg_asBowler)
	lavg_asFielder.append(avg_asFielder)
	lavg_d11sc.append(avg_d11sc)

	lstd_asBataman.append(std_asBataman)
	lstd_asBowler.append(std_asBowler)
	lstd_asFielder.append(std_asFielder)
	lstd_d11sc.append(std_d11sc)

	lwavg_asBataman.append(wavg_asBataman)
	lwavg_asBowler.append(wavg_asBowler)
	lwavg_asFielder.append(wavg_asFielder)
	lwavg_d11sc.append(wavg_d11sc)
	
	lwstd_asBataman.append(wstd_asBataman)
	lwstd_asBowler.append(wstd_asBowler)
	lwstd_asFielder.append(wstd_asFielder)
	lwstd_d11sc.append(wstd_d11sc)
	player.append(PlayerName)
	lastBatsman=PlayerName
	pd.DataFrame({"Last_batsman":PlayerName},index=range(0,1)).to_csv("Last.csv",index=False)


dt["Matches"] = lno_of_matches
dt["Player"] = player
dt["Avg_Bats"] = lavg_asBataman
dt["Avg_Bowler"] = lavg_asBowler
dt["Avg_field"] = lavg_asFielder
dt["Avg_Total"] = lavg_d11sc
dt["stdBat"] = lstd_asBataman
dt["stdBowl"] = lstd_asBowler
dt["stdFiekd"] = lstd_asFielder
dt["stdDr11"] = lstd_d11sc

dt["wAvg_Bats"] = lwavg_asBataman
dt["wAvg_Bowler"] = lwavg_asBowler
dt["wAvg_field"] = lwavg_asFielder
dt["wAvg_Total"] = lwavg_d11sc
dt["wstdBat"] = lwstd_asBataman
dt["wstdBowl"] = lwstd_asBowler
dt["wstdFiekd"] = lwstd_asFielder
dt["wstdDr11"] = lwstd_d11sc

dt.to_csv("Finale.csv")
print (df.head)