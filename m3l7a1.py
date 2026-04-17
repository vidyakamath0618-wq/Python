#implemination of two player tic tac toe game in python
'''we will make the board using dictionary in which keys will be the location(i.e:top-left, mid-right,etc.)and initially the values will be empty space and then after every move we will change the value according to player's choice of move.'''
theboard = {'7':'', '8':'', '9':'', '4':'', '5':'', '6':'', '1':'', '2':'', '3':''}
board_keys = []
for key in theboard:
    board_keys.append(key)
    '''we will have to print the updated board after every move in the game and thus we will make a function in which we will define the printBoard function so we can easily print the board everytime by calling this function.'''
    def printboard(board):
        print(board['7']+'|'+board['8']+'|'+board['9'])
        print('-+-+-')
        print(board['4']+'|'+board['5']+'|'+board['6'])
        print('-+-+-')
        print(board['1']+'|'+board['2']+'|'+board['3'])
    #now we will write the main function which has all the gameplay functionality
    def game():
            turn = 'x'
            count = 0
            for i in range (10):
                 printboard(theboard)
                 print("its your turn,"+turn+".move to which place?")
                 move = input()
                 if theboard[move]=='':
                      theboard[move] = turn
                      count+=1
                 else:
                      print("that place is allready filled.\nmove to which place?")
                      continue
                 #now we will check if player X or O has one for every move after 5 moves
                 if count>=5:
                      if theboard['7']== theboard['8']==theboard['9']!='':#across the top
                           printboard(theboard)
                           print("\ngame over.\n")
                           print("****"+turn+"won.****")
                           break
                      elif theboard['4']== theboard['5']==theboard['6']!='':#across the middle
                           printboard(theboard)
                           print("\ngame over.\n")
                           print("****"+turn+"won.****")
                           break
                      elif theboard['1']== theboard['2']==theboard['3']!='':#across the bottom
                           printboard(theboard)
                           print("\ngame over.\n")
                           print("****"+turn+"won.****")
                           break
                      elif theboard['1']== theboard['4']==theboard['7']!='':#across the middle
                           printboard(theboard)
                           print("\ngame over.\n")
                           print("****"+turn+"won.****")
                           break