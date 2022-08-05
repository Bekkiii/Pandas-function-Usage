import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=index_labels)
df1 = df.iloc[1] #selecting single row
df2 = df.iloc[:,1] #selecting a single column
df3 = df.iloc[[1,2]] #selecting multiple rows
df4 = df.iloc[:,[0,2]] #selecting multiple columns
df5 = df.iloc[0:2] #selecting row range
df6 = df.iloc[:,0:2] #selecting column range
df7 = df.iloc[0:4:2] #selecting alternate rows
df8 = df.iloc[:,0:3:2] #selecting alternate columns
df9 = df.iloc[list(df['Fee']>=25000)]
