import pandas as pd
import numpy as np
technologies = ({
    'Courses':["Spark",np.nan,"pandas","Java","Spark"],
    'Fee' :[20000,25000,30000,22000,np.NaN],
    'Duration':['30days','40days','35days','60days','50days'],
    'Discount':[1000,2500,1500,1200,3000]
               })
df = pd.DataFrame(technologies)
val = df.mean() # Calculate mean
val1 = df.mean(numeric_only=True) # Calculate mean for all non numeric columns
val2 = df[['Discount', 'Fee']].mean() # mean() on selected columns
val3 = df.mean(axis=0, numeric_only=True, skipna=True) # Skip NaN Values

