import pandas as pd
import numpy as np
data = [(3,5,7), (2,4,6),(5,8,9)]
df = pd.DataFrame(data, columns = ['A','B','C'])
def add_4(x):
    return x+4
df['B'] = df['B'].apply(add_4) # Using apply function single column
df2 = df.apply(add_4)
df3 = df[['A','B']].apply(add_4)
df4 = df.apply(lambda x: x + 10)
df5 = df['A'].apply(lambda x: x+10)
df6 = df.apply(lambda x: np.square(x) if x.name in ['A','B'] else x) # Apply function NumPy.square() to square the values of two rows
#why is it used 'x.name' cant it be used solo x

