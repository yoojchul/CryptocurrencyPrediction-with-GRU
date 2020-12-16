import json
import pandas as pd

with open("bitcoin-2018-2020-full.json", "r") as f:
    d = json.load(f)
df = pd.DataFrame(d)

original_columns=[u'close', u'date', u'high', u'low', u'open']
new_columns = ['Close','Timestamp','High','Low','Open']
df = df.loc[:,original_columns]
df.columns = new_columns
df.to_csv('bitcoin-2018-2020-full.csv',index=None)
