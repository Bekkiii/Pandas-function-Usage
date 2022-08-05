import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark",np.nan,"pandas","Java","Spark"],
    'Fee' :[20000,25000,30000,22000,26000],
    'Duration':['30days','40days','35days','60days','50days'],
    'Discount':[1000,2500,1500,1200,3000]
               })
df = pd.DataFrame(technologies, index = ['r1','r3','r5','r2','r4'])
df1 = df.sort_values('Courses') # Default sort
df2 = df.sort_values('Courses', ascending=False) # Sort by Descending
df3 = df.sort_values(by=['Courses', 'Fee']) # Sory by multiple columns
df4 = df.sort_values(by='Courses', ignore_index=True) # Sort and ignore index
df5 = df.sort_values(by=['Courses', 'Fee'], na_position='first') # Sory by putting NaN at first
df6 = df.sort_values(by='Courses', key=lambda col: col.str.lower()) # Sort by function 'misunderstanding'

