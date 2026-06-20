# ============================================================
# FILE: main.py
# ============================================================
import pygame
import sys
from board import Board
from constants import WINDOW_SIZE, BOARD_SIZE, SQUARE_SIZE, WHITE, BLACK

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Chessboard Display")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.selected_square = None  # (row, col) or None
        self.valid_moves = []         # list of (row, col)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.handle_click(event.pos)

            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_click(self, pos):
        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return

        clicked_piece = self.board.get_piece(row, col)

        # If a piece is already selected
        if self.selected_square is not None:
            # If clicking on a valid move target
            if (row, col) in self.valid_moves:
                # Move the piece (placeholder – move validation later)
                self.board.move_piece(self.selected_square[0], self.selected_square[1], row, col)
                self.selected_square = None
                self.valid_moves = []
                return

            # If clicking on own piece, re-select it
            if clicked_piece and clicked_piece.color == self.board.turn:
                self.selected_square = (row, col)
                self.valid_moves = self.board.get_valid_moves(row, col)  # will be implemented later
                return

            # Otherwise deselect
            self.selected_square = None
            self.valid_moves = []
            return

        # No selection yet: select if own piece
        if clicked_piece and clicked_piece.color == self.board.turn:
            self.selected_square = (row, col)
            self.valid_moves = self.board.get_valid_moves(row, col)  # will be implemented later

    def draw(self):
        self.screen.fill(WHITE)
        self.board.draw(self.screen)
        # Draw selection highlight
        if self.selected_square is not None:
            row, col = self.selected_square
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            s.fill((255, 255, 0, 80))  # semi-transparent yellow
            self.screen.blit(s, rect)
        # Draw valid move dots
        for (r, c) in self.valid_moves:
            center = (c * SQUARE_SIZE + SQUARE_SIZE // 2, r * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(self.screen, (100, 200, 100, 180), center, 12)

if __name__ == "__main__":
    game = ChessGame()
    game.run()
