#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np

# Welcome messages
def welcome():
    print('Welcome to my TicTacToe Python game!\n')
    print('Let get started! For start the first player digit the coordenates as: row column (Ex.: 0 2)')
    print('The accepted values are 0, 1 or 2 for rows or columns.')
    print('Please player 1 start the game or press q to quit the game.\n')

# Print the Matrix
def printMatrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

# Loop the playing
def play():

    # Dictionary with the players
    players = [
        {
            'player': 1,
            'symbol': 'x'
        },
        {
            'player': 2,
            'symbol': 'o'
        }
    ]

    # Index to loop the players
    index = 0

    while(True):

        printMatrix(matrix)
        input_coordenates = input('\n (P{}) Coordenates: '.format(players[index%2]['player']))

        if len(input_coordenates) > 0:
            coordenates = input_coordenates.split()            

            if (type(coordenates[0]) is str) and coordenates[0] == 'q':
                print('See you next time! ;)')
                break

            elif len(coordenates) == 2:
                row = int(coordenates[0])
                col = int(coordenates[1])

                if 0 <= row <= 2 and 0 <= col <= 2:
                    if matrix[row][col] != ' ':
                        print('Not empty, try again.')
                    else:
                        matrix[row][col] = players[index%2]['symbol']
                    
                    if checkWinner(matrix,players[index%2]['symbol']):
                        printMatrix(matrix)
                        print('Congractulations Player {}, you Win!!!'.format(players[index%2]['player']))
                        break
                    else:
                        # Increment index
                        index += 1
                else:
                    print('Sorry, only accept tow values between 0 and 2... ;)\n')
            else:
                print('Not a valid input... Try again!')

# Check for a Winner
def checkWinner(matrix, symbol):
    
    # Rows and Columns
    for index in range(3):
        if check(matrix[index,:],symbol):
            return True
        if check(matrix[:,index],symbol):
            return True

    # Diagonal
    if check(np.diag(matrix),symbol):
        return True
    
    # Inverted Diagonal
    if check(np.diag(np.fliplr(matrix)),symbol):
        return True

    return False

# Verify if all the itens in the row are equal to the playre's symbol
def check(row,symbol):
    return np.all([row[i] == symbol for i in range(len(row))])

# Main
if __name__ == '__main__':

    # Initialize the Matrix with empty Strings and fill it with 'x' ou 'o' during the game
    matrix = np.array([[np.str(' ') for rows in range(3)] for columns in range(3)])

    # Welcome message
    welcome()
    
    # Start the game
    play()
