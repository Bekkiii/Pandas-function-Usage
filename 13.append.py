import pandas as pd

df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                    'Fee': [25000,25200,24500,24900],
                    'Duration': ['30days','35days','40days','45days']})
df2 = df.append(df1) # Using append() method
'''The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  df2 = df.append(df1) # Using append() method'''