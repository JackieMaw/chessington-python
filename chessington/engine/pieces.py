"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        available_moves = []

        if self.player == Player.WHITE:            
            current_square: Square = board.find_piece(self)
            if (current_square.row < 7):

                next_square = Square.at(current_square.row + 1, current_square.col)
                if (board.get_piece(next_square) == None):
                    available_moves.append(next_square)

                if (current_square.row == 1):
                    following_square = Square.at(current_square.row + 2, current_square.col)
                    if (board.get_piece(next_square) == None) and (board.get_piece(following_square) == None):
                        available_moves.append(following_square)

                diagonal_square_left = Square.at(current_square.row + 1, current_square.col + 1)
                if (board.get_piece(diagonal_square_left) != None):
                    available_moves.append(diagonal_square_left)

                diagonal_square_right = Square.at(current_square.row + 1, current_square.col - 1)
                if (board.get_piece(diagonal_square_right) != None):
                    available_moves.append(diagonal_square_right)
                
        else:
            current_square: Square = board.find_piece(self)
            if (current_square.row > 0):
                next_square = Square.at(current_square.row - 1, current_square.col)
                if (board.get_piece(next_square) == None):
                    available_moves.append(next_square)
                if (current_square.row == 6):
                    following_square = Square.at(current_square.row - 2, current_square.col)
                    if (board.get_piece(next_square) == None) and (board.get_piece(following_square) == None):
                        available_moves.append(following_square)

        return available_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []