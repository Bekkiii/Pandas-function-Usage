import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,np.nan,1200],
    'Start_Date' : ['2021-02-04 05:30:00','01-09-2021 06:30:00',
                    '2021-03-06 07:30:00']
              }

df = pd.DataFrame(technologies)
index_labels = ['r1','r2','r3']
df.index =index_labels # Set list to index
df2 = df.set_index('Courses') # Set single colin as index
df2 = df.set_index('Courses', append=True) # Append index
df3 = df.set_index(['Courses','Duration']) # Set multiple columns as Index
df4 = df.set_index(pd.DatetimeIndex(pd.to_datetime(df['Start_Date'])))