import pandas as pd
import numpy as np
technologies= {
    'Fee' :[22000,25000,23000,np.NaN,26000],
    'Duration':['30days','50days','30days','35days','40days']
          }
df = pd.DataFrame(technologies)
df['Fee'] = df['Fee'].map(lambda x:x-(x*10/100))  #Using Lambda Function
df['Fee'] = df['Fee'].map('{} RS'.format) # Let's add the currently to the Fee
df['Fee'] = df['Fee'].map('{} RS'.format,na_action='ignore') # Use na_action param
dict_map = {'30days':'35 Days','50days':'55 Days','40days':'45 Days'}
updateSer = df['Duration'].map(dict_map) # Using Dictionary for mapping
df['Duration'] = updateSer