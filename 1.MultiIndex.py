import pandas as pd
multi_index = pd.MultiIndex.from_tuples([("r0", "rA"),("r1", "rB")],names=['Courses','Fee'])
cols = pd.MultiIndex.from_tuples([("Gasoline", "Toyoto"), ("Gasoline", "Ford"),  ("Electric", "Tesla"), ("Electric", "Nio")])
data=[[100,300, 900,400 ], [200,500, 300,600]]
df = pd.DataFrame(data, columns=cols,index=multi_index)
df2 = df.reset_index(level=[1]) # MultiIndex to Single Index by dropping
df.columns = df.columns.get_level_values(1)# Flattern MultiIndex columns
df3 = df.droplevel(0,axis=0) #Drop Index from MultiIndex
