## USED STRICTlY TO UPDATE DB

import sqlite3 
import score 

from score import *
from sqlalchemy import *
from stadium import *

db = create_engine('sqlite:///./score/score.db')

df = pd.DataFrame({"Away " : away, "away_score" : away_score, "Home": home, "home_score": home_score, "time": time})


df.to_sql(tosqlfile, db,'sqlite',if_exists='replace')


