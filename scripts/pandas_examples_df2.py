import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20160101', periods=10)

print("\n------Pandas Dataframe")
tab10n5 = np.random.randn(10,5)
df = pd.DataFrame(tab10n5, index=dates, columns=['A','B','C','D','E'])
print(df)

print("\n------Pandas Dataframe selection: 'A'")
print(df['A'])

print("\n------Pandas Dataframe selection: df[0:3]")
print(df[0:3])

print("\n------Pandas Dataframe selection by label location: df.loc[:,['A','B']")
print(df.loc[:,['A','B']])

print("\n------Pandas Dataframe selection by label location: df.loc['20160102':'20160104',['A','B']]")
print(df.loc['20160102':'20160104',['A','B']])

print("\n------Pandas Dataframe selection by index location: df.iloc[3]")
print(df.iloc[3])

print("\n------Pandas Dataframe selection by index location: df.iloc[[1,2,4],[0,2]]")
print(df.iloc[[1,2,4],[0,2]])

print("\n------Pandas Dataframe selection by index location: df.iloc[1:3,:]")
print(df.iloc[1:3,:])

print("\n------Pandas Dataframe selection by Conditionals: df[df.D > 0]")
print(df[df.D > 0])



#Joins

left = pd.DataFrame({'key': ['a', 'b', 'c'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key': ['a', 'c', 'd'], 'rval': [4, 5, 6]})
#print(left)
#print(right)
#print(pd.merge(left, right, on='key'))

#Group
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                             'foo', 'bar', 'foo', 'foo'],
                      'B' : ['one', 'one', 'two', 'three',
                             'two', 'two', 'one', 'three'],
                      'C' : np.random.randn(8),
                      'D' : np.random.randn(8)})

#print(df.groupby('A').sum())
#print(df.groupby(['A','B']).sum())
