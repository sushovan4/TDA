# %%
# Definite Loops
# Python knows how many times to go around
# Syntax
#-------------------------------------------------------------------------------
# for <var> in <seq>:
#   <body>
#-------------------------------------------------------------------------------
# <var>: loop index
# <seq>: sequence of values, usually a list / array 
# <body>: task to execute in every iteration


#%%
# for val in string :
print("\nLoop through the characters in a string:")
for char in 'GW Rocks' :
  print(char)


#%%
# for <val> in <list>:
print("\nLoop through the days of the week:")
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for day in days:
  print(day) # mind the tab / indentation

# %% 
# Use enumerate to print the indices
# Read: https://docs.python.org/3/library/functions.html#enumerate
for index, day in enumerate(days):
  print(f"{index}: {day}") # mind the tab / indentation
#
#


#%%
# Now for dictionary
# for val in dictionary : (keys only)
print("\nLoop through key, val in dictionary??")
adictionary = { "k0": 4, "k8": '2', "k1": ("a",5), "k5": 'end' }
for key in adictionary :
  print('key:', key)


# %%
# Activity - 1
# Modify the code above to print the key/value pairs
for key in adictionary :
  print(f'key: {key}, value: {adictionary[key]}')

#



# %%
type( enumerate([1,2]) )

#%%
# or try this for dictionary, using .items() to get the pairs
print("\nalternative method to loop thru key, val in dictionary:")
# adictionary.items(): creates a object type of dict_items, which can be looped 
# through as key/value pairs   
for key, val in adictionary.items() :
  # print("key:", key, "value:", val, "type of value", type(val))
  print(f"key: {key}, value: {val}, and type of val: {type(val)}" )


# %%
# Activity 3: Accumulating results
# Compute the factorial of 5 using a for loop
prod = 1
for i in [1, 2, 3, 4, 5]:
  prod *= i
print(prod) 
# 
# 
#  


# %%
# Activity 4: User defined range
# Modify the above program to write a generic code that compute the factorial
# of any given integer
n = 5   
prod = 1
for i in range(n):
  prod *= (i + 1)
print(prod) 
#


# %%
# Activity 5: Using range differently
# Find the sum of the first n (positive) odd numbers
# Hint: range(start, end, step)  
n = 50   
sum = 0
for i in range(1, 2 * n, 2):
  sum += i
print(sum) 
#


# %%
# Activity (bonus): Add numbers without using for loops
# Find the sum of the first 100 even numbers 
n = 50
sum = n * (2 * 1 + (n - 1) * 2) // 2 # a = 1, d = 2
print( sum )

#