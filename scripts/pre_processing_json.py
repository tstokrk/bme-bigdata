import pandas as pd
import urllib, json

url = "https://data.seattle.gov/resource/pu5n-trf4.json"
with urllib.request.urlopen(url) as response:
    data = response.read()

data_json = json.loads(data.decode())
df_all = pd.DataFrame(data_json)

df = df_all.loc[:,['event_clearance_date',
                   'event_clearance_group']]

df = df.dropna(how='any')

# Simple global stat
stat1 = pd.value_counts(df['event_clearance_group'].values, sort=True)
print(stat1)

# Simple group by stat
df['event_clearance_date'] = pd.to_datetime(df['event_clearance_date'])
df_SL = df[(df.event_clearance_group == 'SHOPLIFTING')]
df_SL = df_SL.set_index('event_clearance_date')
df_SL.sort_index(inplace=True)
df_SL['year'] = df_SL.index.year
s_SL = df_SL.groupby(['year'])['event_clearance_group'].value_counts()
print(s_SL)