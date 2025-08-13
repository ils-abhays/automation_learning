values = [1, 2, "abhay", 1.5, 11]

print(values) # [1, 2, "abhay", 1.5, 11]
print(type(values)) # list
print(values[0]) # indexing starts from 0

print((values[1:3])) # [2 , "abhay"]
# This is the list slicing operation. It extracts a portion of the list values based on the specified indices.
# 1: This is the start index. Slicing begins at the element at index 1
# 3: This is the end index. Slicing goes up to but does not include the element at index 3.

values.insert(3, "sankhere") # insert the value in particular index
values.append(50) # append the value at the last of the list
del values[-2] # here "-" indicated the indexing from the end and "2" indicates second last value.
# del is using for delete the value of particular index.
values[2] = "ABHAY" # here we are updating the value of index 2

print(values) # [1, 2, 'ABHAY', 'sankhere', 1.5, 50]
