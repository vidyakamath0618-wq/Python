#take input of a word
string=input("please enter your own word:")
#take input of a character
char=input("please enter your own character")
i = 0
count = 0
#loop will to find the occurence of character
while(i<len(string)):#string operation
    if(string[i]== char): #condition1
        count = count+1
    i = i + 1
#display the result
print("the total number of times", char,"has occured=", count)
