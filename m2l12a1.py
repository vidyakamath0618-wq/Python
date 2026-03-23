import random #importing module
playing = True #initialise
number = str(random.randint(0,9))#random in-built function
print("i will generate a number from 0 to 9, and you will have to guess the number one digit at a time")
print("the game ends when you get 1 hero!")
#iterate loop until condition is true
while playing:
    guess = input("give me your best guess !\n")
    if number == guess:
        print("you win the game!")
        print("the number was",number)
        break
    else:
        print("your guess isnt quite right,try again.\n")