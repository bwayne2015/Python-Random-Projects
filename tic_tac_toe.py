import random
def inputletter():
    #This Funtion Give player the choice his Letter and Assignes the other one to the computer
    letter = ""
    while not(letter =='X' or letter=='O' ):
        letter = input("Please choose one letter (x or o)")
        letter = letter.upper()
        print(letter)
    if letter =='X':
        return ['X','O']
    else:
        return ['O','X']    
def first_move_decision():
    #This function decides and return who first Starts the game
    first_move = random.randint(0,1)
    if first_move == 1:
        return "player"
    else:
        return "computer"
def draw_the_board(game_board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3])
    print('   |   |')

def get_player_move(game_board):
    #Get Players move and return as integer
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not is_free_space(game_board, int(move)):
        move = input("Please Enter your Next Move[1,9] : ")
    return int(move)
def is_free_space(board,move):
    #This checks whether any Free space avaliable in the board and return True
    return board[move] == " " 

def make_move(game_board,letter,move):
    game_board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def istie(game_board):
    #checks The game has been Tied
    for item in range(1,10):
        if is_free_space(game_board,item):
            return False    
    return True
def choose_position_manually(board,position_list):
    possible_move = []
    for item in position_list:
        if is_free_space(board,item):
            #print("inside")
            possible_move.append(item)
            #print(possible_move)

    if len(possible_move) != 0 :
        return random.choice(possible_move)
    else:
        return None 



def board_copy(game_board):
    copylist = []
    for item in game_board:
        copylist.append(item)
    return copylist    
    
def get_comp_move(game_board,comp_letter):
    #This is the computer AI program to decide the computer's Move
    # First Computer Checks Whether it can win on the next Move he will make
    if comp_letter == "X":
        player_letter = "O"
    else:
        player_letter ="X"
    #STEP 1 :     
    #The below for loops checks every single move from computer whether it can win in one move
    for item in range(1,10):
        #checks in the copy not in actual list
        copy = board_copy(game_board)
        #print(copy)
        if is_free_space(copy,item):
            #print(copy)
            #print(comp_letter)
            #print(item)
            make_move(copy,comp_letter,item)
            if isWinner(copy,comp_letter):
                return item

    # Check if the player could win on his next move, and block them.
    #STEP 2
            
    for item in range(1,10):
        copy = board_copy(game_board)
        if is_free_space(copy,item):
            make_move(copy,player_letter,item)
            if isWinner(copy,player_letter):
                return item
    #print("About to execute Corner position ")

#Try to take any of the corner position :
# Step : 3
    move = choose_position_manually(game_board,[1,3,7,9])
    #print( " Hi " ,move)
    if move != None:
        return move

#Try to take central position :
#Step : 4
    if is_free_space(game_board,5):
        return 5

#Move one of the side position
#step : 5
    move = choose_position_manually(game_board,[2,4,6,8])
    return move

    







print("WELCOME TO TIC TAC TOE !!!!!!!!!!!!!")
while True : 
    #Reset the Board
    game_board = [" "] * 10
    #The below line is assign one one Letter to player and comp
    player_letter,comp_letter = inputletter()
    #print(player_letter)
    #print(comp_letter)
    #Decide who first Starts the game
    turn = first_move_decision()
    print( "The first chance is given to the " + turn)
    game_playing = True
    
    while game_playing:
        if(turn == "player"):
            print("Player's Turn")
            draw_the_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board,player_letter,move)

            if isWinner(game_board,player_letter):
                draw_the_board(game_board)
                print("Hooray! You have won the game!")
                game_playing = False
            elif istie(game_board):
                draw_the_board(game_board)
                print("The game has been tied")
                break
            else:
                turn = "computer"
        else:
            # Computer's turn.
            print("Computers turn")      
            move = get_comp_move(game_board,comp_letter)
            #print(move)
            make_move(game_board,comp_letter,move)
            if isWinner(game_board,comp_letter):
                draw_the_board(game_board)
                print("Sorry! you lost the Game!!!")
                game_playing=False 
            elif istie(game_board):
                draw_the_board(game_board)
                print("The game has been tied")
                break
            else:
                turn = "player"
                       

        

