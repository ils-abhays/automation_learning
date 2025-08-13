from logging import NOTSET

age = 25
height = 5.9
favorite_color = "blue"
male = True

print(f"Age: {age} | Type: {type(age)}") # integer
print(f"Height: {height} | Type: {type(height)}") # float
print(f"Favorite Color: {favorite_color} | Type: {type(favorite_color)}") # string
print(f"Gender: {male} | Type: {type(male)}") # boolean

# Notes---------
# The f prefix allows you to embed expressions (variables, calculations, function calls, etc.) directly within a string literal by enclosing them in curly braces {}.
# These expressions are evaluated at runtime, and their values are inserted into the string.
#
# f-strings make string formatting more readable and concise compared to older methods like the % operator or the .format() method.
# You can see the variables and expressions directly within the string, making it easier to understand the intended output.