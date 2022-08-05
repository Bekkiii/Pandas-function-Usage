import pandas as pd
technologies= {
    'Courses':["Spark","PySpark","Spark","Java","PySpark","PHP"],
    'Fee' :[22000,25000,23000,24000,26000,27000],
    'Duration':['30days','50days','30days','60days','35days','30days']
          }
df = pd.DataFrame(technologies)
df1 = df.filter(items=['Courses','Fee']) #filter columns by labels
df2 =df.filter(like='ration',axis=1) #Filter Columns using like
df3 = df.filter(regex='e$', axis=1) # Filr column names by regex
df4 = df.filter(items=[0,2],axis=0) #filter rows with indices

