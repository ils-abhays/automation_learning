# if-else condition

text = "Good Morning"
a = 2

if text == "Morning":
    print("Condition Matches")
else:
    print("Condition do not matches")

print("------First Loop is over------")

if a < 4:
    print("------Second Loop is started------")
    print("Condition Matches")
else:
    print("Condition do not matches")

# for loop
print("************FOR LOOP IS STARTED*************")
obj = [2, 3, 4, 6, 8, 9]  # Interate each and every element of the list and print
for i in obj:
    print(i) # all the items of the list as it is
    print(i*2) # all the items after multiply by 2

print("---------second for loop Program started --------")
# Sum of first natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1,6): # if range is (i,j) ten it will iterate i to j-1
    summation = summation + j
print(summation) # print must be outside from the loop. If it is present inside then print values in each iterations.

print("---------third for loop Program started --------")
# Skipping indexes and jump specific interval then pass value as a third argument.

for i in range(1,10,2): # skip values after every 2 intervals
    print(i)

print("---------third for loop Program started --------")
# if only upper range is provided then it will starts from 0 index
for i in range(10):
    print(i)

print("************** WHILE LOOP IS STARTED ****************")
print("---------Infinite while loop Prog-1 -------")
# a = 5

# while a>1:
    # print(a)
# while loop stops when condition becomes false
a = 5
while a>1:
    print(a)
    a = a - 1
print('while loop execution done')

print("---------While loop Prog-2 -------")

# If we have to skip value without using break keyword
a = 5

while a>1:
    if a != 3:
        print(a)
    a = a - 1
print("while loop execution is done")

print("---------While loop Prog-3 -------")

# If we have to skip value using break keyword
a = 5

while a>1:
    if a == 3:
        break
    print(a)
    a = a - 1
print("while loop execution is done")

print("---------While loop Prog-4 -------")

# If we have to skip current iteration and execute next iteration using continue keyword
a = 10

while a>1:
    if a == 9:
        a = a - 1
        continue
    if a == 3:
        break
    print(a)

    a = a - 1
print("while loop execution is done")