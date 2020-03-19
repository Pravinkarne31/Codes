import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

url = 'https://covid.ourworldindata.org/data/full_data.csv'

df = pd.DataFrame(pd.read_csv(url, index_col='location'))
Full_Data = df
#print(df['date'].max())
df=df.drop(['World','International'], inplace=False)

df = df[df['date'] == df['date'].max()].sort_values(by='total_cases', ascending=False)
df=df[:10]
df=df.drop(['date','new_cases','new_deaths'], axis=1)

df.plot.bar(rot =70,title="Top 10 Countries by Total Cases")

plot.show(block=True)
