# ============================================================
# FILE: pieces.py
# ============================================================
import pygame
from constants import SQUARE_SIZE, WHITE, BLACK

class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol  # e.g., 'P', 'N', 'B', 'R', 'Q', 'K'

    def draw(self, screen, row, col):
        # In a real implementation, you would load images.
        # Here we use simple text for clarity and portability.
        font = pygame.font.SysFont("Arial", SQUARE_SIZE // 2, bold=True)
        text = font.render(self.symbol, True, self.color)
        text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                          row * SQUARE_SIZE + SQUARE_SIZE // 2))
        screen.blit(text, text_rect)

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, "P")

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, "R")

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, "N")

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, "B")

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, "Q")

class King(Piece):
    def __init__(self, color):
        super().__init__(color, "K")
