# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1             # int
# y = 2.5           # float
# name = 'Aaron Mikhail Salud'     # string
# is_active = True    # bool

# Multiple assigment
x, y, name, is_active = (7, 4.5, 'Aaron Mikhail Salud', True)

print(x, y, name, is_active)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

# Check type
print(type(z))
print(z)
