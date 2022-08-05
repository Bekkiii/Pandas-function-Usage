import pandas as pd
df = pd.DataFrame (
    dict(Courses=['Spark', 'Python', 'Java'], Fee=[22000, 25000, 23000, ], Duration=['30days', '50days', '30days']))
df2 = df[df['Courses'].isin(['Spark'])] # Specific Value
df3 = df[df['Courses'].isin(['Spark','Java'])] # List of Values
df4 = df.isin(['Spark', 'Python', 23000, '50days'])# isin() with list of values
df5 = df.isin({'Courses':['Spark','Python']}) # check by column name
df22 = pd.DataFrame({
    'Courses' :['C++','Python',],
    'Fee' :[23000,25000,],
    'Duration':['30days','55days']
          })
df6 = df.isin(df22)