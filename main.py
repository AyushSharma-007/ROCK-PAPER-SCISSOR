print("-------------WELCOME TO THE GAME OF ROCK PAPER SCISSOR------------")
counta = 0
countb = 0
for i in  range(0,3):
    a = input("Choose you option player-1 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    b = input("Choose you option player-2 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    if a == 'R' and b == 'R' : 
              print('TIE')
    elif a =='R' and b == 'S' : 
              print('PLAYER-1 WINS') 
              counta += 1 
    elif a == 'R' and b == 'P' : 
              print('PLAYER-2 WINS') 
              countb += 1 
    elif a == 'S' and b == 'R' : 
              print('PLAYER -2 WINS') 
              countb += 1 
    elif a == 'S' and b == 'P' : 
              print('player -1 wins') 
              counta += 1 
    elif a == 'S' and b == 'S' : 
              print('TIE')
    elif a == 'P' and b == 'R' : 
              print('PLAYER-1 WINS') 
              counta += 1 
    elif a == 'P' and b == 'P' : 
              print('TIE')
    elif a == 'P' and b == 'S' : 
              print('PLAYER - 2 WINS') 
              countb += 1 
    else:
        print("Enter a valid option")
if counta > countb:
    print("player 1 wins the series")
elif countb>counta:
    print("player 2 wins the series")
else:
    print("Its a tie")
