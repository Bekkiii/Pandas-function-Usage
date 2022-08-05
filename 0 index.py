import pandas as pd
technologies = [ ["Spark",20000, "30days"],
                 ["pandas",20000, "40days"],
               ]
df=pd.DataFrame(technologies)
column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
df.index = pd.Index(['idx1','idx2']) # Set new Index

#print(df)
#print(df.index) # Get Index as Series
#print(df.index.values) # Get Index as List
#print(df.index) # Set new Index
