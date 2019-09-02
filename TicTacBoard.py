"""
    Board class for TicTacToe
"""

class BoardStr:
    def __init__(self, size_x, size_y, fill_char):
        self.size_x = size_x
        self.size_y = size_y
        self.data = [[fill_char] * size_x for _ in range(size_y)]

    def get_value(self, x, y):
        return self.data[y][x]
    
    def set_value(self, x, y, v):
        self.data[y][x] = v

    def __getitem__(self, coord):
        # for 3x3 matrix coordinates from 1 to 9
        coord -= 1
        y = coord // self.size_x
        x = coord - y * self.size_x
        return self.get_value(x, y)

    def __setitem__(self, coord, value):
        coord -= 1
        y = coord // self.size_x
        x = coord - y * self.size_x
        self.set_value(x, y, value)

    def getCopy(self):
        board = Board(self.size_x, self.size_y)
        for j in range(self.size_y):
            for i in range(self.size_x):
                board.data[i][j] = self.data[i][j]
        return board

    def print_board(self):
        for j in range(len(self.data)):
            line = self.data[j]
            for i in range(len(line)):
                if i != len(line)-1:
                    print(line[i], end= '|')
                else:
                    print(line[i])
            if j != len(self.data)-1:
                for i in range(len(line)):
                    if i != len(line)-1:
                        print('-', end= '+')
                    else:
                        print('-')

if __name__ == "__main__":
    board = BoardStr(3, 3, ' ')
    board[1] = '1'
    assert(board[1] == '1')
    assert(board.get_value(0, 0) == '1')
    board[5] = '5'
    assert(board.get_value(1, 1) == '5')
    board.print_board()
