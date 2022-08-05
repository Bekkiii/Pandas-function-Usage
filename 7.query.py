import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df = pd.DataFrame(technologies)
df1 = df.query("Courses == 'Spark'") # Query all rows with Courses equals 'Spark'
value = 'Spark'
df2 = df.query("Courses ==@value") # Query Rows by using Python variable
df3 = df.query("Courses != 'Spark'") # not equals condition
df4 = df.query("Courses in ('Spark','Pyspark')") # Query Rows by list of values
values = ['Spark','PySpark']
df5 = df.query('Courses in @values') # Query Rows by list of values
df6 = df.query('Courses not in @values') # Query Rows not in list of values

