import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
df2 = df.groupby(['Courses']).sum() # Use groupby() to compute the sum
df3 = df.groupby(['Courses','Duration']).sum() # Group by multiple columns
df4 = df.groupby(['Courses', 'Duration']).sum().reset_index() # Add Row Index to the group by result
df5 = df.groupby(by=['Courses'], dropna=False) # Drop rows that have None/Nan on group keys
df6 = df.groupby(by=['Courses'], sort=False).sum() # Remove sorting on grouped results
groupedDF = df.groupby('Courses',sort=False).sum()
sortedDF=groupedDF.sort_values('Courses', ascending=False) # Sorting group keys on descending order
df7 = df.groupby('Courses').apply(lambda x: x.sort_values('Fee')) # Using apply() & lambda
result = df.groupby('Courses')['Fee'].aggregate(['min','max']) # Groupby & multiple aggregations
result1 = df.groupby('Courses').aggregate({'Duration':'count','Fee':['min','max']}) # Groupby & multiple aggregations
