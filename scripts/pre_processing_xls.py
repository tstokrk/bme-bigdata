import numpy as np
import pandas as pd
import json

#XLS

df = pd.read_excel('country-of-birth-london-min.xls', 'Sheet1', index_col=None, na_values=['-'])
print(df)

s = df.loc['Poland',:]
print(s.to_json())


