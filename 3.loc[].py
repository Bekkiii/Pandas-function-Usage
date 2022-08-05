#pandas.DataFrame.loc[] is a property that is used to access a group of rows and columns by label(s) or a boolean array.
import pandas as pd
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=index_labels)
df1 = df.loc['r1'] #selecting single rows
df2 = df.loc[:,'Courses'] #selecting single column
df3 = df.loc[['r2','r3']] #selecting multiple rows
df4 = df.loc[:,['Courses','Fee']] #selecting multiple columns
df5 = df.loc['r1':'r4'] #selecting row range
df6 = df.loc[:,'Courses':'Duration'] #selecting column range
df7 = df.loc['r1':'r4':2] #selecting alternate rows
df8 = df.loc[:,'Courses':'Discount':2] #selsecting alternate columns
df9 = df.loc[df['Fee'] >= 2400] #using condition


