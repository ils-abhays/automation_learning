# In python, function is a group of related statements that perform a specific task.

def greet_me(): # function creation
    print("good morning")

greet_me() # function call
print("outside from first functon")

# parametrize function
def greet_me(name): # catch it the value here while declare the varible
    print("good morning "+name) # concatination of two string values.

greet_me("abhay sankhere") # sending the value from here
print("outside from second functon")

def AddInteger(a, b): # function for adding to intergers
    print(a+b)

AddInteger(2,3)

def SumInteger(a, b):
    return (a*b)     # return keyword is a special statement that you can use inside a function or method to send the function’s result back to the caller.

print(SumInteger(3,3))