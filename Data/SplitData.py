import pandas as pd
import numpy as np

data = pd.read_csv("Data/Bitcoin_tweets.csv")
number_of_chunks = 20

for id, df_i in  enumerate(np.array_split(data, number_of_chunks)):
    df_i.to_csv(f'Data/Split/Bitcoin_tweets_{id}.csv', sep=";")

print(data.columns)