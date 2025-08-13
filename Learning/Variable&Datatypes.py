a=3
print(a) # 3
print(type(a)) # Integer

b="abhay sankhere"
print(b) # abhay sankhere
print(type(b)) # String

c=1.56
print(c) # 1.56
print(type(c)) # Float

d=True
print(d) # True
print(type(d)) # Boolean

x, y, z = 1, 0.5, "test"

# concatination of two different datatype

concat = "{} {}".format("My name is", b) # both the arguments goes into the flower braces respectively.

print(concat) # My name is abhay sankhere

# list is a data type that allows multiple values and can be different data types
values = [1, 2, "hello", 5.5, 3]
print(type(values)) # list

print(values[0]) # 1
print(values[2]) # hello

print(values[-1]) # -1 refers to the last item of the list. It helps when list contains large no. of values

print(values[1:4]) # for getting multiple values from the list. Here upper range index is excluded

values.insert(4, "abhay") # Insert value on particular index
print(values) # [1, 2, 'hello', 5.5, 'abhay', 3]

values.append("sankhere") # Value inserted on the last index
print(values) # [1, 2, 'hello', 5.5, 'abhay', 3, 'sankhere']

values[0] = "hi"  # Here we are replacing the value of particular index
print(values)  # ['hi', 2, 'hello', 5.5, 'abhay', 3, 'sankhere']

del values[0]  # here we are deleting the value of particular index
print(values)  # [2, 'hello', 5.5, 'abhay', 3, 'sankhere']

# tuple similar as list data type buy immutable (updation is not possible)
tup = (1, 2, "abhay", 0.5)
print(type(tup))

print(tup) # (1, 2, 'abhay', 0.5)
print(tup[0]) # 1

# Dictionary {key:value} pair
dic = {"a": 1, "b": "abhay", 2: 0.5}
print(dic["b"]) # abhay = > print(variable_name[key])
print(dic[2]) # 0.5

# Create dictionary dynamically at run time
dict = {}
print(dict) # {} empty dictionary
# Adding value in the dictionary
dict["firstname"] = "Abhay"
dict["Sankhere"] = "Sankhere"
dict["Gender"] = "Male"

print(dict) # {'firstname': 'Abhay', 'Sankhere': 'Sankhere', 'Gender': 'Male'}