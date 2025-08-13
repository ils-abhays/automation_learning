a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

print("--------------------------------------------")

#sum of first 5 natural numbers 1,2,3,4,5 = 15
#range = (a,b) ---> a to b-1
summ = 0
for j in range(1, 6):
    summ = summ + j
print(summ)

print("--------------------------------------------")
# 1 is starting point
# 10-1 is end point
# 2 is index/skip the values after each iteration
for k in range(1, 10, 2):
    print(k)

for m in range(10): #If only have a upper range
    print(m)