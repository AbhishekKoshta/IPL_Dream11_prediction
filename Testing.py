import pandas as pd
import numpy as np
batsman = ['DA Warner','S Dhawan','MC Henriques','Yuvraj Singh','DJ Hooda','BCJ Cutting']

lno_of_matches=[]
lavg_asBataman=[]
lavg_asBowler=[]
lavg_asFielder=[]
lavg_d11sc=[]
lstd_asBataman=[]
lstd_asBowler=[]
lstd_asFielder=[]
lstd_d11sc=[]


for bat in batsman:
 	df = pd.read_csv("{}.csv".format(bat))
 	no_of_matches = len(df)
 	avg_asBataman = df["asBataman"].mean()
 	avg_asBowler = df["asBowler"].mean()
 	wavg_asBataman=np.mean([(i*df["asBataman"][i])/no_of_matches for i in range(no_of_matches)])
 	wavg_asBowler=np.mean([(i*df["asBowler"][i])/no_of_matches for i in range(no_of_matches)])

print (avg_asBataman,
avg_asBowler,
wavg_asBataman,
wavg_asBowler)
# print (df.head())
# print (df["asBataman"].mean())
	# avg_asBataman = df["asBataman"].mean()
	# avg_asBowler = df["asBowler"].mean()

