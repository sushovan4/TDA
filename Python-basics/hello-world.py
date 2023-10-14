# %% 
# This is a comment line
# The first line #%% is a "magic python" command. Some interpreters knows what it is, others just ignore them.
# In our case here, VSCode knows #%% is the beginning of a cell, like Jupyter notebook cells
# We can also specify it as a Markdown cell (see bottom of this file) with #%%[markdown] 


# %%
print("Hello, World!") 


# %% Using Python as a calculator
print(1 + 2) # Addition
print(3 - 2) # Subtraction
print(12 * 2) # Multiplication

print(10 / 3) # Float division
print(10 // 3) # Integer division: quotient
print(10 % 3) # Integer division: remainder

# Read the documentation to know about the following command
# divmod(10, 3) 


# %% Activity - 1
# TODO: Print the summands
# Use the `print` function to print two summands of your choice 
# and their sum seperated by `:` on the same line
# your code here
#
# Hint: Read the documentation of the print function here: 
# https://docs.python.org/3.11/library/functions.html?highlight=print#print



# %%
# Check the type/class of data
# There are three numeric data types
type(-1)  # int (ints are arbitrary precision in Python)
type(0.003) # float
type(3+2j) # complex

# TODO: figure out what's wrong with the output from the three line above.


# %% 
# Boolean data type
type(True)
type(False)


# %%
# Variables in Python
x = 3.12 # This is an assignment
y = 5
z = True

# Can a variable be assigned to another variable?
# y = x
# print(y)

# Can we calculate the square root of a number using var assignments?
# x * x = 2
# print(x) 


# %% 
# Activity - 2
# TODO: swap the values of x, y
x = input('x:')
y = input('y:')
# your code here
# 
#
#
print(x, y) # don't change this line


# %% 
# Basic operators: shorthands
x = 3
x += 2 # same as: x = x + 2
print(x)
# other variants are '*=', '-=', '/=', '%=', '**='



# %%
# Strings
astring = "Thank you"
cnt = 1
pi = 3.141592653589793238462643383279502884197
# In python, 'single' quotes and "double" quotes are the same, as long as you 
# use the same for opening and closing.
# Note: `backtick` is different. Not the same as 'single'/"double" quotes, 
# backtick has been removed now

# Many different ways to print out the same line
print("%d. I want to say %s" % (cnt, astring) )
cnt += 1 
print(cnt, ". I want to say" + astring )
cnt+=1
print(cnt, ". I want to say", astring )
cnt+=1
print("%d. I want to say %s, my sweetie %.3f" % (cnt, astring, pi) )
cnt+=1
print("%d. I want to say %s, my sweetie digit %d" % (cnt, astring, pi) )
cnt+=1
print("%d. I want to say %s, my sweetie long %f" % (cnt, astring, pi) )
cnt+=1
# For python 3.6+, we can use the f-string (string interpolator)
print(f"{cnt}. I want to say {astring}, my sweetie long {pi.__round__(3)}")



# %%
# More references
# see https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
# s-string, d-digit (int), f-float
# 
# side note:  
# for more info on the new python f-string since python 3.6, see
# for example: https://cito.github.io/blog/f-strings/
#
# also, see https://docs.python.org/3/reference/lexical_analysis.html#literals
# for info on f-string, r-string, b-string, etc.
