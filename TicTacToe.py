"""
    Tic-tac-toe. Xs and Os. Board 3x3
    board 0-9 array, numerated from bottom
    TODO: classes Board, Graph, AI, Game
"""

import random
from TicTacBoard import BoardStr

CHOOSE_LETTER = "Ты выбираешь 'X' или 'O'?"
YOUR_NEXT_TURN = "Твой следующий ход (1-9)"
HEADER = "Крестики и нолики"
GOES_FIRST = " ходит первым"
YOU_WIN = "Ты выиграл!"
DRAW = "Ничья"
YOU_LOSE = "Ты проиграл, компьютер выиграл"
PLAY_AGAIN = "Сыграем ещё раз? (да или нет)"
YES_FIRST_LETTER = 'д'
HUMAN = "human"
COMP = "computer"

# Board class for TicTacToe
class TicTacBoard(BoardStr):
    def __init__(self, size_x, size_y):
        BoardStr.__init__(self, size_x, size_y, ' ')

    def isFieldFree(self, coord):
        return self[coord] == ' '

    def isFull(self):
        for line in self.data:
            for v in line:
                if v == ' ':
                    return False
        return True

    def getCopy(self):
        board = TicTacBoard(self.size_x, self.size_y)
        for j in range(self.size_y):
            for i in range(self.size_x):
                board.data[i][j] = self.data[i][j]
        return board

    def print_board(self):
        # vertical inversion
        for j in range(len(self.data)-1, -1, -1):
            line = self.data[j]
            for i in range(len(line)):
                if i != len(line)-1:
                    print(line[i], end= '|')
                else:
                    print(line[i])
            if j != 0:
                for i in range(len(line)):
                    if i != len(line)-1:
                        print('-', end= '+')
                    else:
                        print('-')

# User Interface
class ConsoleUI:
    @staticmethod
    def drawBoard(board):
        board.print_board()

    @staticmethod
    def print(msg):
        print(msg)

    @staticmethod
    def inputChar(msg, ava_symbols):
        # what will player letter: X or O
        letter = ''
        while letter not in ava_symbols:
            print(msg)
            letter = input().upper()
        return letter

    @staticmethod
    def inputInt(msg, pred):
        value = ''
        while not (value.isdigit() and pred(int(value))):
            print(msg)
            value = input()
        return int(value)

    @staticmethod
    def getPlayerMove(msg, pred):
        return ConsoleUI.inputInt(msg, pred)
            
def whoGoesFirst():
    if random.randint(0,1) == '0':
        return COMP
    else:
        return HUMAN

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return (
        # horizontal
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[7] == le and bo[8] == le and bo[9] == le) or
        # vertical
        (bo[1] == le and bo[4] == le and bo[7] == le) or
        (bo[2] == le and bo[5] == le and bo[8] == le) or
        (bo[3] == le and bo[6] == le and bo[9] == le) or
        # diagonal
        (bo[1] == le and bo[5] == le and bo[9] == le) or
        (bo[3] == le and bo[5] == le and bo[7] == le) )

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if board.isFieldFree(i):
            possibleMoves.append(i)
    if possibleMoves:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # AI for TicTac
    # if we have winner position: set there
    for i in range(1,10):
        boardCopy = board.getCopy()
        if boardCopy.isFieldFree(i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # if player will win next step -- block him
    for i in range(1,10):
        boardCopy = board.getCopy()
        if boardCopy.isFieldFree(i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # try set to center
    if board.isFieldFree(5):
        return 5

    # try corner
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    # try set to side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def getCompLetter(playerLetter):
    if playerLetter == 'X':
        return 'O'
    else:
        return 'X'

if __name__ == "__main__":
    ui = ConsoleUI()
    ui.print(HEADER)
    while True:
        # new field
        board = TicTacBoard(3, 3)
        playerLetter = ui.inputChar(CHOOSE_LETTER, ['X', 'O'])
        computerLetter = getCompLetter(playerLetter)
        turn = whoGoesFirst()
        ui.print(turn + GOES_FIRST)
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == HUMAN:
                ui.drawBoard(board)
                move = ui.getPlayerMove(YOUR_NEXT_TURN,
                        lambda x: x > 0 and x < 10 and board.isFieldFree(x) )
                makeMove(board, playerLetter, move)
                if isWinner(board, playerLetter):
                    ui.drawBoard(board)
                    ui.print(YOU_WIN)
                    gameIsPlaying = False
                elif board.isFull():
                    ui.drawBoard(board)
                    ui.print(DRAW)
                    break
                else:
                    turn = COMP
            else: # computer turn
                move = getComputerMove(board, computerLetter)
                makeMove(board, computerLetter, move)
                if isWinner(board, computerLetter):
                    ui.drawBoard(board)
                    ui.print(YOU_LOSE)
                    gameIsPlaying = False
                elif board.isFull():
                    ui.drawBoard(board)
                    ui.print(DRAW)
                    break
                else:
                    turn = HUMAN

        print(PLAY_AGAIN)
        if not input().lower().startswith(YES_FIRST_LETTER):
            break
                
                
                
