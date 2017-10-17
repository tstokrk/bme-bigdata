import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n------Pandas Series - date range")
dates = pd.date_range('20160101', periods=10)
print(dates)

print("\n------Pandas Dataframe")
tab10n5 = np.random.randn(10,5)
df = pd.DataFrame(tab10n5, index=dates, columns=['A','B','C','D','E'])
print(df)

print("\n------Pandas - Dataframe description")
print(df.describe())

print("\n------Pandas - Dataframe head")
print(df.head())

print("\n------Pandas - Dataframe values")
print(df.values)
print("\n------Pandas - Dataframe index")
print(df.index)
print("\n------Pandas - Dataframe columns")
print(df.columns)
