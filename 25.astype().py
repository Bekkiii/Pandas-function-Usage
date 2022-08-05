import pandas as pd
import numpy as np
# Create DataFrame from Dictionary
technologies = {
    'Fee' :["20000","25000","26000"],
    'Discount':["1000","2300","1500"]
              }
df = pd.DataFrame(technologies)
df1 = df.astype(int) # Cast all columns to int
df2 = df.astype('int64')
df3 = df.astype('string')# Cast all columns to string
df4 = df.astype('float') # Cast all columns to float
df5 = df.Fee.astype('int') # Cast specific column type

# Create DataFrame from Dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :["20000","25000","26000"],
    'Duration':['30day','40days','35days'],
    'Discount':["1000","2300","1500"]
              }

df11 = pd.DataFrame(technologies)
df6 = df11.astype({'Courses':'string','Fee':'int','Discount':'float'})
df7 = df.Courses.astype('int')