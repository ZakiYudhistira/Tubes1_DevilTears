from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class MyBot(BaseLogic):
    def __init__(self):
        # Initialize attributes necessary
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def next_move(self, board_bot: GameObject, board : Board):
        # Calculate next move
        delta_x = 1
        delta_y = 0
        return delta_x, delta_y

