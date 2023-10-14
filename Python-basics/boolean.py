# Boolean Operators
# Combine relational operators to form complex conditionals

# %%
# Two-way decisions: if elif elif else....
# 
# if <condition 1>:
#  <statement 1>
# elif <condition 2>:
#   <statement 2>
# . . . 
# else :
#  <the last statement>


# %%
# Number to letter grade
grade = 50
if grade >= 93:
    print('A')
elif grade >= 90:
    print('A-')
elif grade >= 87:
    print('B+')
elif grade >= 83:
    print('B')
elif grade >= 80:
    print('B-')
elif grade >= 77:
    print('C+')
elif grade >= 73:
    print('C')
elif grade >= 70:
    print('C-')
else:
    print('F')


# %%
# Example
# Check if an integer is odd or divisible by 5
x = 20
if x % 2 != 0:
    print('success')
elif x % 5 == 0:
    print('success')
else:
    print('failure')


# %%
# The operators can be mixed arbitrarily, but Python will process
# them according to their precedence. 
# Strong to weak: not, and, or
# Syntax: <P> <operator> <Q>


# %%[markdown]
# | P | Q | P `or` Q | P `and` Q | `not` P |
# |---|---|----------|-----------|---------|
# | T | T | T        | T         | F       |
# | T | F | T        | F         | F       |
# | F | T | T        | F         | T       |
# | F | F | F        | F         | T       |



# %%
# Activity - 1
# Rewrite the above code using operators
x  = 20
if (x % 2 != 0) or (x % 5 == 0):
    print('success')
else:
    print('failure')


# %%
# Activity - 2
# Precedence (strong to weak): not, and, or
a, b, c = True, False, False
a or not b and c
#
#


# %% DeMorgan's Law
# (not (a or b))  == ((not a) and (not b))
# (not (a and b)) == ((not a) or (not b))

# %%
# Activity - 3
# Check if a given positive integer is a leap year.
def isLeapYear(year):
    if year < 1:
        print('Enter a positive year')
        return 
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
