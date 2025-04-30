def printboard(board):
    print(board['TL']+"|"+board['TM']+"|"+board['TR'])
    print("-+-+-")
    print(board['ML']+"|"+board['MM']+"|"+board['MR'])
    print("-+-+-")
    print(board['LL']+"|"+board['LM']+"|"+board['LR'])

def win(board,turn):
    winingchoice=[['TL','TM','TR'],['ML','MM','MR'],['LL','LM','LR'],['TL','ML','LL'],['TM','MM','LM'],['TR','MR','LR']]
    for combination in winingchoice:
        x=combination[0]
        y=combination[1]
        z=combination[2]
        if(board[x]==board[y]==board[z] and board[x]!=' '):
            print("*game over")
            if(turn):
                print("*PLAYER 1 WON")
            else:
                print("*PLAYER 2 WON*")
            return True
        return False
    
board={'TL':' ','TM':' ','TR':' ',
       'ML':' ','MM':' ','MR':' ',
       'LL':' ','LM':' ','LR':' '}
turn=True
printboard(board)
for i in range(9):
    if(turn):
        print("PLAYER 1 CHOICE")
    else:
        print("PLAYER 2 CHOICE")
    pos=(input("Enter the position"))
    if(board[pos])==' ':
        if(turn):
            board[pos]='x'
            turn=False
        else:
            board[pos]='o'
            turn=True
    printboard(board)
    winner=win(board,board)
    if(winner):
        break