L = [10,5,18,2,6,3,7,8,9]
print("original list:", L)
#variable to store the sum of 
#the list
count = 0
#finding the sum
for i in L:
    count += i
#divide the total elements by
#number of elemets
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
#sorting the elemets of the list
L.sort()
#printing the first element
print("smallest elemet is:", L[0])
#printing the last element
print("largest elemet is:", L[-1])