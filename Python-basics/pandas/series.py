# %%
# Pandas: https://pandas.pydata.org/docs/index.html
# `Series` is an important data structure provided by Pandas 

# %%
# Installation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
# Empty series
s1 = pd.Series()
print( s1 )


# %%
# Series from a constant or a Python list
s = pd.Series([3.5] * 5)
print(s)


# %%
s = pd.Series('GW Rocks')
# s = pd.Series(list('GW Rocks'))
print(s)


# %%
# Series from an ndarray
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)


# %%
# Series with custom index
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index = [3, 2, 1, 0])
print(s)


# %%
# Series from a dictionary
data = {'0' : 'a', '1' : 'b', '2' : 'c', '3': 'd'}
s = pd.Series(data)
print(s)

# %%
# Data-index mismatch (the preference is on index)
data = {'0' : 'a', '1' : 'b', '2' : 'c', '3': 'd'}
s = pd.Series(data, index = [2, '1'])
print(s)



# %%
# Guess what would happen
s = pd.Series(-2, index=[0, 1, 2, 3])
# s = pd.Series(['A', 'B'], index=[0, 1, 2, 3])
print(s)


# %%
# Extract values and the index
s = pd.Series(range(8), index = list('GW Rocks'))
print(s)
print(type(s))
print(s.index)
print(type(s.index))
print(s.values)
print(type(s.values))
print(type(s.dtype))


# %%
# Annotating a series
s = pd.Series(range(8), index = list('GW Rocks'))
s.index.name = 'Char'
s.name = 'My series'
print(s)


# %%
# Activity: Random series
# Write a function to output the Fibonacci sequence of length n as a series. 
# Name the series and the index appropriately  
def fibSeries(n):
    pass



# %%
# Accessing/slicing a series using the index
s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
print(s['c']) # series is dict-like
# print (type( s['c']) )
# print(s['a':'c'])


# %%
# Integer-based indexing
# Note: 
# - unlike ndarrays, slicing is inclusive
# - it also slices the index
s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
print(s.iloc[0])
# print(s.iloc[:3])


# %% 
# Vectorized operations with series
s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
print(s + s)
print(s  ** 2)
print( np.log10(s) )
print(s.isnull())


# %%
# Label alignment (union of indices)
s = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
s.iloc[1:] + s.iloc[:-1]


# %%
