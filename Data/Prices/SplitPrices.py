import numpy as np
import pandas as pd

data = pd.read_csv("BTCEUR.csv")
number_of_chunks = 2

for id, df_i in  enumerate(np.array_split(data, number_of_chunks)):
    df_i.to_csv(f'BTCEUR_{id}.csv', sep=";", index=False)
    
