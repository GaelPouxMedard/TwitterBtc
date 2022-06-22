import numpy as np
import pandas as pd

def Prices(candles):
    p_time=[]
    p_open=[]
    p_high=[]
    p_low=[]
    p_close=[]
    p_volume=[]

    for i in range(len(candles)):
        p_time.append(candles[i][0])
        p_open.append(float(candles[i][1]))
        p_high.append(float(candles[i][2]))
        p_low.append(float(candles[i][3]))
        p_close.append(float(candles[i][4]))
        p_volume.append(float(candles[i][5]))

    p_time=np.array(p_time)
    p_open=np.array(p_open)
    p_high=np.array(p_high)
    p_low=np.array(p_low)
    p_close=np.array(p_close)
    p_volume=np.array(p_volume)

    x = {"Time": p_time,"Open": p_open, "High": p_high, "Low": p_low, "Close": p_close, "Volume": p_volume}

    X = pd.DataFrame(x)
    return(X)
