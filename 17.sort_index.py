import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark",np.nan,"pandas","Java","Spark"],
    'Fee' :[20000,25000,30000,22000,26000],
    'Duration':['30days','40days','35days','60days','50days'],
    'Discount':[1000,2500,1500,1200,3000]
               })
df = pd.DataFrame(technologies, index = [101,123,115,340,100])
df1 = df.sort_index() # Default sort by index labels
df2 = df.sort_index(ascending=False) # Sort by Descending order
df3 = df.sort_index(ignore_index=True) # Sort ignoring index

