import random #importing random module
while True: #iterate loop
    user_action = input("enter a choice(rock,paper,scissor):")#take input
    possible_action = ["rock","paper","scissor"]
    #using random function
    computer_action = random.choice(possible_action)
    print(f"\n You chose{user_action},computer chose{computer_action}.\n")
    #display both outputs what is selected by you and computer
    #condition to check who won the game
    if user_action == computer_action:
        print(f"both players selected{user_action}It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors!You win!")
        else:
            print("paper covers rock!you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock!you win!")  
        else:
            print("scissors cut paper!you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cut paper!you win!")
        else:
            print("rock smashes scissors!You lose.")
#take input for playing again
    play_again = input("play again?(y/n):")
    if play_again !="y":
        break