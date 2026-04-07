#initialize dictionary
test_dictionary = {"codingal":2, "is": 2, "best":2,"coding":1}
#printing original dictionary
print("the orriginal dictionary:"+ str(test_dictionary))
#initialize value
K  = 2
#using loop
#selective key values in dictionary
res = 0
for key in test_dictionary:
    if test_dictionary[key]== K:
        res = res + 1
#printing result
print("frequency of K is:"+ str(res))