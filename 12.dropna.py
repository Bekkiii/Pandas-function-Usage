import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas",np.nan],
    'Fee' :[20000,25000,26000,23093,24000,np.nan],
    'Duration':['30day','40days','35days','45days',np.nan,np.nan],
    'Discount':[1000,np.nan,1200,2500,pd.NaT,np.nan],
    '':[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
              }
index_labels=['r1','r2','r3','r4','r5','']
df = pd.DataFrame(technologies,index=index_labels)
df1 = df.dropna(how='all') # Drop rows that has all Nan Values
df2 = df.dropna(how='all',axis=1)# Drop columns that has all Nan Values
df3 = df.dropna() # Drop rows that contains nan values
df4 = df.dropna(subset=['Courses', 'Duration'])
df5 = df.dropna(thresh=2)