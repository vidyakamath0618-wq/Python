#input a word or a sentence
string = input("please enter your own string:")
string2=("")
#loop for printing in reverse
for i in string:
    string2 = i + string2
print("\nthe original string=", string)
print("\nthe reversed string=", string2)