import numpy as np

class QuoridorState:
    def __init__(self, board_size=9):
        if board_size % 2 == 0:
            raise ValueError("Board size must be odd")
        
        self.board_size = board_size

        # pawn_board is board_size x board_size
        # pawn_board spec:
        # 0 = no pawn
        # -1, 1 = pawns
        # wall_board is (board_size-1) x (board_size-1)
        # wall board spec:
        #   0 = no wall
        #   -1 = horizontal wall
        #   1 = vertical wall
        self.pawn_board = np.zeros((board_size, board_size), dtype=int)
        self.wall_board = np.zeros((board_size-1, board_size-1), dtype=int)

    @staticmethod
    def from_s_notation(notation: str):
        '''
        s notation - string representation of the board
        Details:
            (board size)-(pawn 1)(pawn 2)-(wall 1)(wall 2)...
        ex) 9-a0i8-a2b4h3...
        '''
        state = QuoridorState()
        notation:tuple = notation.split('-')
        print(notation)


if __name__ == "__main__":
    state = QuoridorState()
    state.from_s_notation("9-a0i8-a2b4h3")