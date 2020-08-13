def display_board(board):
    pos=7
    print('Here is the current game board')
    for j in range (3):
        print('  |   |  ')
        print(f'{board[pos]} ',end="")
        pos+=1
        print(f'| {board[pos]} |',end="")
        pos+=1
        print(f' {board[pos]}')
        print('  |   |  ')
        print('            ')
        pos-=5

def position_choice(board):
    position="Wrong"
    lis=[i for i in range(1,10)]
    value=False
    while position.isdigit()==False or int(position) not in lis or value==False:
        position=input("Enter your next postion between(1-9): ")
        if position.isdigit()==False:
            print("Enter the position in numeric form: ")
        if position.isdigit():
            if int(position) not in lis:
                print("You are out of range! ")
            else:
                if board[int(position)] not in ['X','O']:
                    value=True
                else:
                    print('Position Occupied! Enter a new position. ')
                
    return int(position)

def replacement_value(board,value,position):
    board[position]=value
    return board
    

def gamecontinue_choice():
    choice='wrong'
    print('Do you wish to continue playing? ')
    while choice not in ['Y','N']:
        
        choice=input("Enter your choice between Y or N: ")
        if choice not in ['Y','N']:
            print("You are out of range")
    if choice=='Y':
        return True
    else:
        return False

def player_inpchoice():
    player1='wrong'
    
    while player1 not in ['X','O']:
        player1=input('Player 1: Pick an input of your choice (X or O)? ')
        if player1 not in ['X','O']:
            print('Input is Invalid! ')
    if(player1=='X'):
        player2='O'
    else:
        player2='X'
    
    return (player1,player2)

from random import shuffle
def choose_turn():
    list=[1,2]
    shuffle(list)
    if list[0]==1:
        return 1
    else:
        return 2
    
def result_chk(board,player1,player2):
    for k in range(1,10,3):
        if board[k]==board[k+1]==board[k+2] and board[k]!=' ':
            if board[k]==player1:
                return player1
            else:
                return player2
    for k in range(1,4):
        if board[k]==board[k+3]==board[k+6] and board[k]!=' ':
            if board[k]==player1:
                return player1
            else:
                return player2
    if board[1]==board[5]==board[9] and board[1]!=' ':
        if board[1]==player1:
            return player1
        else:
            return player2
    
    if board[3]==board[5]==board[7] and board[3]!=' ':
        if board[3]==player1:
            return player1
        else:
            return player2
    f=0
    
    for j in range(1,len(board)):
        
        if board[j] != ' ':
            f=1
        else:
            f=0
    if f==1:
        return 'Tie'
    else:
        return 'Continue'
    
def play(board,first,player1,player2):
    result='Continue'
    turn=first
    while result=='Continue':
        display_board(board)
        position=position_choice(board)
        if turn==1:
            board=replacement_value(board,player1,position)
        else:
            board=replacement_value(board,player2,position)
            
        result=result_chk(board,player1,player2)
        if result in [player1,player2,'Tie']:
            break
        if turn==1:
            turn=2
        else:
            turn=1
    return result

print('Welcome to Tic Tac Toe! ')
game_continue=True
while game_continue:
    board=[' ']*10
    player1,player2=player_inpchoice()
    turn=choose_turn()
    print(f'Player {turn} will go first: ')
    wanna_play=input('Are you ready to play? Enter Yes or No: ')
    if wanna_play=='No':
        print('Game Aborted!')
        break
    result=play(board,turn,player1,player2)
    display_board(board)
    if result != 'Tie':
        print('Congratulations! you have won the game. ')
    else:
        print('Game Tied!')
    game_continue=gamecontinue_choice()
else:
    print('Game Ended!!')
    