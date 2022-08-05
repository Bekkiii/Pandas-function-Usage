import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Spark","Python","PySpark"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[1500,1000,1200,800,1300],
    'Duration':['30days','50days','30days','35days','40days']
          }
df = pd.DataFrame(technologies)
df2= df.where(df.Fee>23000) # Default example
df3 = df.where(df.Fee>23000,'Na')
cond1 = df.Fee>23000
cond2 = df.Discount > 900
df4 = df.where(cond1 & cond2,other='Na') #here on multiple columns & conditions

