import pandas as pd
import numpy as np
# Create DataFrame from dict
df = pd.DataFrame({'Courses':['Spark','PySpark','Java','PHP'],
           'Fee':[20000,20000,15000,10000],
           'Duration':['35days','35days','40days','30days']})
df1 = df.reset_index() # reset index on DataFrame
df2 = df.reset_index(inplace=True, drop=True) # drop index as column
df3 = df.index.name = 'Custom_index' # Set index name
df.index = np.arange(1, len(df)+1) # Reset index starting from 1
