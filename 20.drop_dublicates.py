import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","PySpark","Pandas"],
    'Fee' :[20000,22000,22000,30000],
    'Duration':['30days','35days','35days','50days'],
              }
df = pd.DataFrame(technologies)
df1 = df.drop_duplicates() #drop duplicates
df2 = df.drop_duplicates(subset=['Courses']) #using subset option
