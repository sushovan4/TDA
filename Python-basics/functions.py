# Functions
# A function is a bag or sequence of statements
# Functions facilitate reuse of code
# A function is like a new button on your calculator

# Parts of a functions:
#   identifier or name: usually a legal string
#   inputs: a sequence of arguments
#   body or function definition: indented sequence of Python statements
#   return: a return statement for the output

# Syntax: 
# def <identifier>(<arguments>):
#   <function definition>
#   ...
#   <return>
#


# %%
# Hello world as a function
def helloWorld():
  print('Hello world!')
#


# %%
# Call the function here and from the interactive session.
helloWorld()
#

# %%
# Add a formal argument to the function definition 
# <greeting> is a formal parameter, a placeholder
def helloWorld1(greeting):
  print(f'{greeting}: hello world!')


# %%
# Call `helloWorld2` with actual parameters
helloWorld1('Good morning')


# %% 
# Activity - 1a
# Write a program (without a function) to detect a negative number in a list
list1 = [0 , 1, -2, 3, -1]
list1 = [0 , 1, 5, 2, 0, 3]

flag = False
for i in list1:
  if i < 0:
    flag = True

print('Has negatives') if flag else print('No negatives')


# %%
# Activity - 1b
# Now create a function to do the same
# Do you see an advantage of using a function
def hasNegative(list):
  for num in list:
    if num < 0:
      return True    
  
  return False
#
#



# Activity 2:
# Write a function that computes the discriminant of a quadratic equation.
# Equation: ax^2 + bx + c = 0
# import math
def discriminant(a, b, c):
  return b * b - 4 * a * c

#
#


## %%
# Activity 2a:
# Call your function with some arguments.
discriminant(1, 2, 3)



# %%
# Activity 2b:
# What happens if you change the order of the arguments?
# Call your function with formal parameters. In that case, order of parameters
# would not matter.
discriminant(c = 3, a = 1, b = 2)
#



# %%
# Activity 3: 
# Using a function inside another function
# Write a function to tell if a quadratic equation has complex roots or real 
# roots
# 1: real distinct roots, 0: double roots, -1: complex roots
def roots(a, b, c):
  D = discriminant(a, b, c)
  if D > 0:
    return 1
  elif D == 0:
    return 0
  else:
    return -1
#
#



# %%
# Activity 3a: The White House
# address = '1600 Pennsylvania Ave., Washington, D.C., 20500'
# Write a function called `getCity` whose input is an address and output the city
def getCity(addr):
  return addr.split(', ')[1]


# %%
# Activity 3b:
# Similarly, write a function called `getState`
def getState(addr):
  return addr.split(', ')[2]


# Activity 3c:
# Write a function that to check if two addresses are in the same city
def sameCity(addr1, addr2):
  return getCity(addr1) == getCity(addr2) and getState(addr1) == getState(addr2)
#
#



# %% 
# Activity 4:
# Write a function to compute the GCD (greatest common divisor) of two integers
#
def findGCD(n, m):
    if n < 1 or m < 1:
        print('Please enter positive numbers')
        return 
    
    res = 1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            res = i
    return res



# Scope of a variable: global vs local

#%%
# global variables vs local scope
thisMonth = 'Sept' # this is a global variable

# %%
# 1. Functions have access to global variables
def func():  
  return thisMonth
print( func() )

# %%
# 2. Assignment creates a local variable
def func():  
  thisMonth = thisMonth + 'ember'
  return thisMonth
print( func() )

# %%
# 3. Assignment creates a local variable
thisMonth = 'Sept' # this is a global variable
def func():
  thisMonth = 'Dec'  
  thisMonth = thisMonth + 'ember'
  return thisMonth
print( 'Local: ' + func() )
print('Global: '  + thisMonth)


# %%
# 4. Modify global vars with the `global` keyword
thisMonth = 'Sept' # this is a global variable
def func():
  global thisMonth
  thisMonth = 'Dec'  
  thisMonth = thisMonth + 'ember'
  return thisMonth
print( 'Local: ' + func() )
print('Global: '  + thisMonth)
# %%
