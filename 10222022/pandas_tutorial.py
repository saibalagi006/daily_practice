########### This is going to contain all important function of pandas 
## adapted from https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#object-creation

import pandas as pd
import numpy as np 

## create series 

s = pd.Series([1,2,3,4,np.nan])

dates = pd.date_range("20221022",periods=10)

df = pd.DataFrame(np.random.randn(10,4),dates,columns=list("ABCD"))

#print(df)

#df.head()

df.tail(3)

