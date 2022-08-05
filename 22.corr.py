import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Spark","Python","PySpark"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1500,1000,1200,800,1300],
    'Duration':['30days','50days','30days','35days','40days']
          }
df = pd.DataFrame(technologies)
corr = df['Fee'].corr(df['Discount'])# Correlation between two columns of DataFrame.
df2 =df.corr() # Correlation between all the columns of DataFrame.
df['Fee'] = np.float64(df['Fee'])


