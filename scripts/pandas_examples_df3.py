import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Joins

print("\n------Pandas Dataframe Joins")
left = pd.DataFrame({'key': ['a', 'b', 'c'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key': ['a', 'c', 'd'], 'rval': [4, 5, 6]})

print("\n------Pandas Dataframe LEFT")
print(left)
print("\n------Pandas Dataframe RIGHT")
print(right)
print("\n------Pandas Dataframe Merged LEFT with RIGHT")
print(pd.merge(left, right, on='key'))


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                      'B' : ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                      'C' : np.random.randn(8),
                      'D' : np.random.randn(8)})

print("\n------Pandas Dataframe df.groupby('A').sum()")
print(df.groupby('A').sum())

print("\n------Pandas Dataframe df.groupby(['A','B']).sum()")
print(df.groupby(['A','B']).sum())
