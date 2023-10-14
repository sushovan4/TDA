# %%
import pandas as pd
import numpy as np

# %%
# Pandas Dataframes
# It's a 2D labeled data structure
df = pd.DataFrame()
print (df)


# %%
# Dataframe from a list
df = pd.DataFrame(['a', 'b', 'c', 'd', 'e'])
print(df)


# %%
# Dataframe from a list of lists
data = [['apples', 10],['orange', 20],['Bananas', 30]]
df = pd.DataFrame(data, columns = ['Name', 'Count'])
print(df)


# %%
# Dataframe from dict of lists
data = { 
   'Name': ['apples', 'orange', 'Bananas'], 
   'Count' : [10, 20, 30] 
}
# df = pd.DataFrame(data)
df = pd.DataFrame(data, index = ['a','b','c'])
print(df)


# %%
print('type(data) :')
print(type(data))
print('df :')
print(df)
print('type(df) :')
print(type(df))
print('df.values :')
print(df.values)
print('type(df.values) :')
print(type(df.values))
print(df.values.dtype)

# %%
# Dataframe from a list of dicts
data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]
df = pd.DataFrame(data, index = ['first', 'second'])
# df = pd.DataFrame(data, index = ['first', 'second'], columns = ['a', 'b'])
# df = pd.DataFrame(data, index = ['first', 'second'], columns=['a', 'bb']) # forced
print(df)


# %%
# Dataframe from pd series
df = { 
   'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([3, 2, 1], index=['a', 'b', 'd'])
}
df = pd.DataFrame(df)
print(df)


# %%
# Index / selection
# Note: treat a df like a dictionary of a like-indexed series
df = { 
   'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([3, 2, 1], index=['a', 'b', 'd'])
}
df = pd.DataFrame(df)
print(df)
print('#' * 50)

# %%
# print( df['one']) # column selection by label -> Series
# print( df.loc['a'] ) # row selection by label -> Series
# print(df.iloc[1]) # row selection by int index -> Series
print( df[2:3] ) # slice rows -> DataFrame


# %%
# Column deletion
del(df['one']) #Danger
print(df)


#%%
# Slicing dataframes
df = pd.DataFrame({'value':[10, 20, 30, 40],
                  'patient':[1, 1, 1, 2],
                  'disease':['Flu', 'Cancer', 'Infection','Aneurysm']})
print(df)

print(df.iloc[1:2]) # range, -> DataFrame
print(df.iloc[[0, 2], 0:2]) # list, -> DataFrame



# %%
# Data alignment
df1 = pd.DataFrame(np.random.rand(4, 3), 
                   columns = ['a', 'b', 'c'], 
                   index = ['first', 'second', 'third', 'fourth'])
print( df1 )



# %%
# Guess what would happen
# This operation broadcast row-wise
print( df1 - df1.iloc[0] ) ##



# %%
# Arithmetic operations via alignment (union or columns and indices)
df2 = pd.DataFrame(np.random.rand(3, 2), 
                   columns = ['b', 'c'], 
                   index = ['first', 'second', 'fourth'])
print( df2 )
print( df1 + df2 )



# %%
# Boolean operations
# Explain the output
df1 ** 2 > df1



# %%
# Transposing
df1.T




# %%
# Pandas Statistics support
d = {'Name':pd.Series(['a', 'b', 'c', 'd']),
     'Age':pd.Series([10, 15, 20, 30]),
     'Rating':pd.Series([4, 3, 2, 1])}

df = pd.DataFrame(d)
df

# %%
print(df.sum()) # col sum

print(df.sum(1)) # row sum

# print(df.mean())
# print(df.std())
# print(df.count())
# print(df.min())
# print(df.median())
# print(df.mode())
# print(df.cumsum())
# print (df.describe(include='all'))



# %%
# String support
s = pd.Series(['Superman', 'Spider Man', 'Hello', '@gmail','1234','Sillyman'])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print(s.str.strip())
print(s.str.split(' '))
print(s.str.cat(sep='-'))
print(s.str.get_dummies())
print(s.str.contains('@'))
print(s.str.replace('@','-'))
print(s.str.count('m'))
print(s.str. startswith ('S'))
print(s.str.endswith('4'))
print('#',50*"-")

################################################################
# %%
# Some Other Statistical functions 
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.rand(3, 2))
print(df.pct_change())
s1 = pd.Series(np.random.rand(10))
s2 = pd.Series(np.random.rand(10))
print(s1.cov(s2))

df = pd.DataFrame(np.random.randn(3, 3), columns=['a', 'b', 'c'])
print(df['a'].cov(df['b']))
print(df.cov())

df = pd.DataFrame(np.random.randn(15, 3),
index = pd.date_range('1/1/2019', periods=15),
columns = ['A', 'B', 'C'])




# %%
# Activity: Simulation
# Toss n coins simultaneously repeatedly for m time, 
# and record the outcomes in a dataframe
n = 100
m = 50000
df = pd.DataFrame(np.random.randint(0, 2, (m, n)))
df



# %%
# Add a column to sum with the row means
df = df.assign( mean = df.mean(1))
df


# %%
# Plot the histogram of means
df.hist(column = 'mean', bins = 50)





# %%
# Iterating through a dataframe
df = pd.DataFrame({
   'A': np.linspace(0, 20, 20), # look at the col
   'B': np.random.rand(20),
   'D': np.random.normal(100, 10, size=(20))
})
print(df)

# Iterate through the column names
for col in df:
   print(col)

# Iterate through the row names
for row_index, row in df.iterrows():
   print (row_index, row)



# %%
# Sorting
df1=pd.DataFrame(np.random.rand(3, 2), 
                 index = [1, 6, 4],
                 columns = ['col2', 'col1'])
print(df1)

df2 = df1.sort_index() # sorting the index
df3 = df1.sort_index(ascending = False) # sorting the index
df4 = df1.sort_index(axis = 1) # sorting the column names
df5 = df1.sort_values(by = 'col1') # sorting by columns
df5 = df1.sort_values(by = ['col1', 'col2']) # sorting by multiple cols
# Explain how this works

df6 = df1.sort_values(by='col1', kind = 'mergesort') # sorting algo used


print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print('#',50*"-")



#%%
# Missing values
df = pd.DataFrame(np.random.randn(5, 3), 
                    index=['a', 'c', 'e', 'f', 'h'],
                    columns=['one', 'two', 'three']
                    )
print(df)


df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)

# %%
print(df['one'].isnull())
print(df['one'].notnull())
print(df['one'].sum()) # Ignores NaN
print(df.fillna(0))


# %%
# Cleaning up na values
print(df.dropna())



# %%
print(df.dropna(axis = 0)) # drops columns 
# print(df.dropna(axis = 1)) # drops rows
print('#',50*"-")


# %%
# Concatenate
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)
df = pd.concat([df1, df2, df3], keys = ['x', 'y', 'z']) # adds a hierarchical index
# df.loc['y'].loc['4']

# %%
# Change `axis` and `join` method
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
df2 = pd.DataFrame(
    {
        "B": ["B4", "B5", "B6", "B7"],
        "D": ["D4", "D5", "D6", "D7"],
        "F": ["F4", "F5", "F6", "F7"],
    },
    index=[4, 5, 6, 7],
)
pd.concat([df1, df2], keys = ['x', 'y'], axis = 0, join = 'outer')


# %%
# Merging is different from concatenating
# Same as joining db tables
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }

)
pd.merge(left, right) # contrast pd.concat([left, right], axis = 1)
# pd.merge(left, right, on = 'key')

# %%
# Duplicate columns
# How to join?
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2"],
        "A": ["A0", "A1", "A2"],
        "B": ["b0", "b1", "b2"],
    }
)
right = pd.DataFrame(
    {
        "key": ["K0","K2", "K3"],
        "B": ["B0","B2", "B3"],
        "C": ["C0","C2", "C3"],
        "D": ["D0","D2", "D3"],
    }

)
pd.merge(left, right, on = 'key', how = 'inner') 




# %%
# Extra: Group a dataframe
ipl_data = {
   'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
   'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
   'Points' : [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
df = pd.DataFrame(ipl_data)
print(df)
print(df.groupby('Team').groups)
print(df.groupby(['Team','Year']).groups)

grouped = df.groupby('Year')
for name,group in grouped:
    print(name)
    print(group)
print(grouped.get_group(2014))
print(grouped['Points'].agg(np.mean))
grouped = df.groupby('Team')
print(grouped.agg(np.size))
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))
print(df.groupby('Team').filter(lambda x: len(x) >= 3))
print('#',50*"-")
