# Write a Python program to build a tic-tac-toe game.

board =  ["[     ]","[     ]","[     ]","[     ]","[     ]","[     ]","[     ]","[     ]","[     ]"]


def print_board():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])


def move(Player):
    a = input("This is {}'s turn.Choose a position (1-9): ".format(Player))    
    while True :
        b = a.strip()
        if b.isdigit():
            b = int(b)
            if ((b >= 1) and (b <= 9)):
                if board[b - 1] == "[     ]" :
                    if Player == "Player1" :
                        board[b - 1] = "[ X ]"
                    if Player == "Player2" :
                        board[b - 1] = "[ O ]"                    
                    break
                else :
                    print("That space is already taken!")
                    a = input("Please choose a position which is unoccupied: ")
            else :
                print("{} is not valid.".format(a))
                a = input("Enter an integral number between 1 and 9: ")
        else :
            print("{} is not valid.".format(a))
            a = input("Enter an integral number between 1 and 9: ")
    
def is_victory(icon):
    if ((board[0] == board[1]  == board[2] == icon) or  \
        (board[3] == board[4]  == board[5] == icon) or \
        (board[6] == board[7]  == board[8] == icon) or \
        (board[0] == board[3]  == board[6] == icon) or \
        (board[1] == board[4]  == board[7] == icon) or \
        (board[2] == board[5]  == board[8] == icon) or \
        (board[0] == board[4]  == board[8] == icon) or \
        (board[2] == board[4] == board[6] == icon)):
      return True
    
def is_draw():
    if ((board[0] == board[1] == board[2] == board[3] == board[4] == board[5] == board[6] == board[7] == board[8] != "[     ]" )):        
        return True
    else :
        return False
# This function NEVER will return True because ALL the elements in the list "board" will NEVER be SAME ELEMENTS (i.e., neither completely X, nor completely O).


def is_draw():
    if  "[     ]" not in board :        
        return True
    else :
        return False


    
while True :
    print_board()
    if is_victory("[ O ]")== True :
        print("Player2 wins. Congratulations!")
        break
    elif is_draw()== True :
        print("It's a draw!")
        break
    move("Player1")
    print_board()    
    if is_victory("[ X ]")== True :
        print("Player1 wins. Congratulations!")
        break
    elif is_draw()== True :
        print("It's a draw!")
        break
    move("Player2")
