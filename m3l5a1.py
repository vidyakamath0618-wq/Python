#different types of sets in python
#set of integers
my_set = {1,2,3}
print(my_set)
#set of mixed data types
my_set = {1.0,"Hello",(1,2,3)}
print(my_set)
#set cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)
#we can make set from a list
my_set = set([1,2,3,2])
print(my_set,"\n")
#remove a number from set
num_set = set({0,1,2,3,4,5})
print("Original set:")
print(num_set)
num_set.pop()
print("after removing the first elemet from the said set:")
print(num_set,"\n")