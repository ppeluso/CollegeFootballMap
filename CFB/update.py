from score import *
from sqlalchemy import *
from datetime import datetime
startTime = datetime.now()

#do something

db = create_engine('sqlite:////Users/peterpeluso/desktop/CFB/score/score.db')

df = pd.DataFrame({"Away ": away, "away_score": away_score, "Home": home,
                  "home_score": home_score, "time": time})


# old = pd.read_sql(tosqlfile, db)
# df.to_csv(file, index=False)
# df.to_sql(tosqlfile, db, 'sqlite', if_exists='replace')
# new = pd.read_sql(tosqlfile, db)
#print(pd.DataFrame.equals(new, old))

# changedids = new.index[np.any(new != old, axis=1)]

# print(changedids)

stad = pd.read_sql('stadium', db)
hold1 =[]
hold2 = []
for i in range(len(home)):
	for j in range(len(stad['Team'])):
		if home[i] == stad["Team"][j]:
			
			hold1.append(stad["Lat"][j])
			hold2.append(stad['lng'][j])
			break
	else:
		hold1.append("NaN")
		hold2.append("NaN")



potatframe = pd.DataFrame({"Away": away, "away_score": away_score, "Home": home,
                  "home_score": home_score, "time": time, "lat": hold1, 'lng': hold2})

potatframe.to_sql(tosqlfile, db, 'sqlite', if_exists='replace')

potatframe.to_json("./data.json")

data_array = []
for i in range(len(potatframe["Away"])):
	data_array.append({'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
		'lat': potatframe["lat"][i],
		"lng": potatframe["lng"][i],
		'infobox': "{away}:{away_score} \n {home}: {home_score}".format(away = potatframe["Away"][i], 
																					away_score = potatframe["away_score"][i],
																					home = potatframe["Home"][i],
																					home_score = potatframe["home_score"][i] )
		})

print(data_array)

print datetime.now() - startTime

