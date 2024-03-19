# GUESS THE NUMBER

import random

name=input("Enter the name of the player= ")
a=random.randint(1,20)
i=1
n=6
c=0

while i<=7:
    c=c+1
    b=int(input("\nEnter the value u think computer has guessed = "))
    if (a>b):
        
        n=n-1
        print("\nYour guess is too low, you have ",n," guess remaning")
    elif(b>a):
        n=n-1
        print("\nYour guess is too high you have ",n," guess remaning")
    else:
        print("YOU WON !! YOUR GUESS IS CORRECT")
        print("Your Guess = ",b,"\n Computers guess= ",a)
        print("\nYou took ",c," number of attempts to guess the number")
        break
    i=i+1
    
    
# Quiz
print("Are you Ready to playe quiz Yes or NO ???")
q=input("")
c=0
if(q=='Yes') or (q=='yes'):
    print("\nWhat is my name ??")
    a=input("")
    if(a=='Kashish') or (a=='kashish'):
        print("Correct Answer")
        c=c+1
        print(c)
    else:
            print("Wrong Answer")
    
    print("\nWhat do i like the most to eat ??")
    b=input("")
    if(b=='Pizza') or (b=='pizza'):
        print("Corrent Answer ")
        c=c+1
        print(c)
    else:
            print("Wrong Answer")

    print("\nWhat is my Finace's name??")
    d=input("")
    if(d=='devki') or (d=='Devki'):
        print("Correct Answer")
        c=c+1
        print(c)
    else:
            print("Wrong Answer")
    print("\nCongratulations you have finished the quiz and you have given",c,"Correct Answers")
    print("\nThe average of your correcnt answers is ",100/c,"%")
    print("\nBYE")
else:
    print("Thank You for your time")


# Tic tac toe

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" ** " +turn + " won. **")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
    