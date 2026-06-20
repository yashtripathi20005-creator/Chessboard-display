# ============================================================
# FILE: board.py
# ============================================================
import pygame
from constants import BOARD_SIZE, SQUARE_SIZE, LIGHT_SQUARE, DARK_SQUARE, WHITE, BLACK
from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = WHITE  # White moves first
        self.setup_pieces()

    def setup_pieces(self):
        # Back row (row 0 = black back rank, row 7 = white back rank)
        back_row_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        # Black pieces (row 0 and 1)
        for col, piece_class in enumerate(back_row_order):
            self.grid[0][col] = piece_class(BLACK)
        for col in range(BOARD_SIZE):
            self.grid[1][col] = Pawn(BLACK)

        # White pieces (row 7 and 6)
        for col, piece_class in enumerate(back_row_order):
            self.grid[7][col] = piece_class(WHITE)
        for col in range(BOARD_SIZE):
            self.grid[6][col] = Pawn(WHITE)

    def get_piece(self, row, col):
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            return self.grid[row][col]
        return None

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.grid[from_row][from_col]
        self.grid[to_row][to_col] = piece
        self.grid[from_row][from_col] = None
        # Switch turn (will be refined with validation later)
        self.turn = BLACK if self.turn == WHITE else WHITE

    def get_valid_moves(self, row, col):
        # Placeholder for move validation – will be implemented later.
        # For now, return all squares around the piece (demo only)
        piece = self.get_piece(row, col)
        if not piece:
            return []
        # This is just a placeholder. Real validation will be added later.
        moves = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                    if self.grid[r][c] is None or self.grid[r][c].color != piece.color:
                        moves.append((r, c))
        return moves

    def draw(self, screen):
        # Draw board squares
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rect)

        # Draw pieces
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.grid[row][col]
                if piece:
                    piece.draw(screen, row, col)
