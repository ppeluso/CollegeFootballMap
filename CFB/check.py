from score import *
from sqlalchemy import *
from test import potatframe
 db = create_engine('sqlite:///./score/score.db')



old = pd.read_sql(tosqlfile, db)
df.to_csv(file, index=False)
df.to_sql(tosqlfile, db, 'sqlite', if_exists='append')
new = pd.read_sql(tosqlfile, db)
print(pd.DataFrame.equals(new, old))

changedids = new.index[np.any(new != old, axis=1)]

print(changedids)
