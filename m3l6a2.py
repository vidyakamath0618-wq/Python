#Zip elements of two lists
s1 = {2,3,1,}
s2 = {'b','a','c'}
s3 = list(zip(s1,s2))
print(s3,"\n")
#zip elements of two lists
#print elemets one by one, but elements in 2nd list will be in reverse order
list1  = [10,20,30,40]
list2 = [100,200,300,400]
for x,y in zip(list1,list2[::1]):
    print(x, y)
#zip into dictionary
stocks = ['reliance','infoys','fcs']
prices = [2175,1127,2750]
new_dict = {stock : prices for stock,
            prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))