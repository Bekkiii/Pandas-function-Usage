import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [0,1,2,4,6,10,4],
                   'B': [0,1,3,6,9,np.nan,4]})
rolling = df.rolling(window=2) # Returns Rolling subclass.
df2 = df.rolling(window=3).sum() # Rolling() of sum with window length 3
df3 = df.rolling(window=3).mean() #Rolling() of mean with window length 3
df4 = df.rolling(window=3, win_type='triang').mean() # Rolling() of sum with win_type triang
df5 = df.rolling(window=3, win_type='gaussian').mean(std=3) # Rolling() of sum with window type gaussian !!!(what is 'std') and why needed
df6 = df.rolling(2).agg({'A': 'sum', 'B':'min'})




