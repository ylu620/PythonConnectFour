from random import randint

class Move:
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y


class Connect4:

    def __init__(self):
        self.numOfCol = 7
        self.numOfRow = 6
        self.numToWin = 4
        self.board = self.getNewBoard()
        self.winner = '.'
        self.curPlayer = '.'
        self.curMove = Move('.', 0,0)




    def insertPiece(self, column, piece):
        # insert Piece at Column
        self.curPlayer = piece
        for y, val in reversed(list(enumerate(self.board[column]))):
            if val == '.':
                print 'piece ', piece, ' dropped at column ', column
                self.board[column][y] = piece
                self.curMove = Move(piece, column, y)
                if self.getWinner() == piece:
                    self.winner = piece
                    print 'Found winner. winner is: ', piece

                return True
        return False  # column full

    def getWinner(self):
        # return Winner
        xStraight = yStraight = 1
        posDiag = negDiag = 1

        x = self.curMove.x
        y = self.curMove.y
        curPiece = self.curMove.player

        for i in range(-3,4):
            if i == 0:
                continue

            if i>= 0:
                if x+i <=self.numOfCol-1:
                    xStraight = xStraight+1 if self.board[x+i][y]==curPiece else 1
                    if y-i >= 0:
                        posDiag = posDiag + 1 if self.board[x+i][y-i]==curPiece else 1
                if y+i <= self.numOfRow-1:
                    yStraight = yStraight+1 if self.board[x][y+i]==curPiece else 1
                if (x+i<=self.numOfCol-1) and (y+i <= self.numOfRow-1):
                    negDiag =negDiag+ 1 if self.board[x+i][y+i]==curPiece else 1
            else:
                if x+i >= 0:
                    xStraight =xStraight+ 1 if self.board[x+i][y]==curPiece else 1
                    if y-i <= self.numOfRow-1:
                        posDiag =posDiag+ 1 if self.board[x+i][y-i]==curPiece else 1
                if y+i >= 0:
                    yStraight = yStraight+ 1 if self.board[x][y+i]==curPiece else 1
                if (x+i >= 0) and (y+i >= 0):
                    negDiag =negDiag + 1 if self.board[x+i][y+i]==curPiece else 1


        # print 'xs: ', xStraight, ' ys:', yStraight, ' pd: ', posDiag, ' nd: ', negDiag
        if xStraight>=self.numToWin or yStraight>=self.numToWin or posDiag>=self.numToWin or negDiag>=self.numToWin:
            return curPiece
        else:
            return '.'


    def getNewBoard(self):
        board = [[]]
        for x in range(self.numOfCol):
            board.append([])
            for y in range(self.numOfRow):
                board[x].append('.')
        return board



    def printBoard(self):

        for x in range(self.numOfCol):
            print x,

        print
        for y in range(self.numOfRow):
            for x in range(self.numOfCol):
                print ' '.join(self.board[x][y]),
            print

    def checkIfBoardFull(self):
        boardFull = True
        for x in range(self.numOfCol):
            if self.board[x][0] == '.':
                boardFull = False
                return boardFull
        print 'Board full! '
        return boardFull

    def simulateRandomGame(self):
        print 'Now simulating a random game, board drawn after each turn'
        self.getNewBoard()
        self.printBoard()

        if randint(1,2) == 1:
            curPlayer = 'O'
        else:
            curPlayer = 'X'

        while(self.winner=='.' and not self.checkIfBoardFull()):
            column = randint(0,6)
            if not self.insertPiece(column, curPlayer):
                pass

            self.printBoard()
            if curPlayer == 'X':
                curPlayer = 'O'
            else:
                curPlayer = 'X'



if __name__ == '__main__':
    game = Connect4()
    print('game initializing')
    game.printBoard()

    game.simulateRandomGame()
    # 4 y straight win
    # game.insertPiece(3, 'O')
    # game.insertPiece(3, 'O')
    # game.insertPiece(3, 'O')
    # game.insertPiece(3, 'O')
    # game.printBoard()
