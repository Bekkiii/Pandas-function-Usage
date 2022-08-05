import pandas as pd
import numpy as np
df = pd.DataFrame(({
     'Courses':["Spark",'Java',"Scala",'Python'],
     'Fee' :[20000,np.nan,26000,24000],
     'Duration':['30days','40days','NA','40days'],
     'Discount':[1000,np.nan,2500,None]
               }))
df2 = df.fillna('None') # fillna to replace all NaN
df2['Discount'] = df['Discount'].fillna('0') # fillna on one column
df2[['Discount', 'Fee']] = df[['Discount', 'Fee']].fillna('0') # fillna() on multiple columns
df3 = df.fillna(value={'Discount': '0','Fee':10000}) # fillna() on multiple columns
df4 =df.fillna(value={'Discount':0,'Fee':0}, limit=1) # fill with limit