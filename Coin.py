from Slot import Slot
import pygame

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BOARD_SIZE = (7,6)


class Coin():
    """A class that represents the coin pieces used in connect 4"""

    RADIUS = 30

    def __init__(self, coin_type):
        """
        Initialize a coin with a given coin_type
        (integer that represents its color)
        """
        self.coin_type = coin_type
        self.surface = pygame.Surface((Slot.SIZE - 3, Slot.SIZE - 3))
        if (self.coin_type == 1):
            self.color = BLUE
        else:
            self.color = RED

    def set_position(self, x1, y1):
        """
        Set the position of the coin on the screen
        """
        self.x_pos = x1
        self.y_pos = y1

    def set_column(self, col):
        """
        Set the column on the board in which the coin belongs
        """
        self.col = col

    def get_column(self):
        """
        Get the column on the board in which the coin belongs in
        """
        return self.col

    def set_row(self, row):
        """
        Set the row on the board where the coin is
        """
        self.row = row

    def get_row(self):
        """
        Get the row on the board in which the coin belongs
        """
        return self.row

    def move_right(self, background, step=1):
        """
        Move the coin to the column that is right of its current column
        """
        self.set_column(self.col + 1)
        self.surface.fill((0, 0, 0))
        background.blit(self.surface, (self.x_pos, self.y_pos))
        self.set_position(self.x_pos + step * Slot.SIZE, self.y_pos)
        self.draw(background)

    def move_left(self, background):
        """
        Move the coin to the column that is left of its current column
        """
        self.set_column(self.col - 1)
        self.surface.fill((0, 0, 0))
        background.blit(self.surface, (self.x_pos, self.y_pos))
        self.set_position(self.x_pos - Slot.SIZE, self.y_pos)
        self.draw(background)

    def drop(self, background, row_num):
        """
        Drop the coin to the bottom most possible slot in its column
        """
        self.set_row(row_num)
        self.surface.fill((0, 0, 0))
        background.blit(self.surface, (self.x_pos, self.y_pos))
        self.set_position(self.x_pos, self.y_pos + ((self.row + 1) * Slot.SIZE))
        self.surface.fill((255, 255, 255))
        background.blit(self.surface, (self.x_pos, self.y_pos))
        self.draw(background)

    def get_coin_type(self):
        """
        Return the coin type
        """
        return self.coin_type

    def draw(self, background):
        """
        Draw the coin on the screen
        """
        pygame.draw.circle(self.surface, self.color, (Slot.SIZE // 2, Slot.SIZE // 2), Coin.RADIUS)
        self.surface = self.surface.convert()
        background.blit(self.surface, (self.x_pos, self.y_pos))
