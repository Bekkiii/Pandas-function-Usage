import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Spark","Java Language","PySpark","PHP Language"],
    'Fee' :[22000,25000,23000,24000,26000,27000],
    'Duration':['30days','50days','30days','60days','35days','30days']
          }
df = pd.DataFrame(technologies)
df2 = df.replace('Spark', 'Apache Spark') # Replace column value
df3 = df.replace(['Spark', 'PySpark'],['Apache Spark', 'Apache PySpark']) # Replace multiple values
df4 = df.replace(['30days', '35days'],'40days')# Replace with same value for multiple
df5 = df.replace({'Courses': 'Apache Spark', 'Duration':'35days'},{'Courses':'Spark','Duration':'40days'})

