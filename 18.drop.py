import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
df2 = df.drop(['Fee'], axis=1) # Drops 'Fee' column
df3 = df.drop(labels=['Fee'], axis=1) # Explicitly using parameter name 'labels'
df4 = df.drop(columns='Fee', axis=1) # Alternatively you can also use columns instead of labels.
df5 = df.drop(df.columns[[1]], axis=1) # Drop column by index.
df6 = df.drop(['Courses', 'Fee'], axis=1) #Drop Two or More Columns By Label Name
df7 = df.drop(df.columns[[0,1]], axis=1) #Drop Two or More Columns by Index
lisCol = ['Courses', 'Fee']
df8 = df.drop(lisCol, axis=1)
for col in df.columns: #Remove Columns from a List of Columns (iteratively) By Condition.
    if 'Fee' in col:
        del df[col]
df9 = df.drop(df.loc[:,'Courses':'Fee'].columns, axis=1) #Using df.loc() to Remove Columns Between Specified Columns
df10 = df.drop(df.iloc[:,1:2], axis=1) #Using df.iloc() to Remove Columns Between Specified Column Indexes.

