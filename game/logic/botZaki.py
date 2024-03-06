import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class BotZaki(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
    
    def getDistance(self, game : GameObject, board_bot : GameObject):
        return abs(board_bot.position.x - game.position.x) + abs(board_bot.position.y - game.position.y)
    
    def getNearestDiamonds(self, board_bot : GameObject, board : Board):
        array_diamond = [diamonds for diamonds in board.diamonds]
        if len(array_diamond) > 0:
            nearest = array_diamond[0]
            tot = self.getDistance(array_diamond[0], board_bot)
            for i in range(1, len(array_diamond)):
                print(array_diamond[i].position.x, array_diamond[i].position.y)
                if self.getDistance(array_diamond[i], board_bot) < tot:
                    tot = self.getDistance(array_diamond[i], board_bot)
                    nearest = array_diamond[i]
            return nearest.position
        else:
            return None
    def getNearestTeleporter(self, board_bot : GameObject, board : Board):
        teleporter = []
        for i in board.game_objects:
            if i.type == "TeleportGameObject":
                teleporter.append(i)
        
    
    def getNearestResetButton(self, board_bot : GameObject, board : Board):
        reset = []
        for i in board.game_objects:
            if i.type == "DiamondButtonGameObject":
                reset.append(i)

    def next_move(self, board_bot : GameObject, board: Board):
        props = board_bot.properties
        # Analyze new state
        if props.diamonds == 5:
            # Move to base
            base = board_bot.properties.base
            self.goal_position = base
        else:
            self.goal_position = self.getNearestDiamonds(board_bot, board)
            print("Going to : ", self.goal_position.x, self.goal_position.y)
            print("Current Pos : ", board_bot.position.x, board_bot.position.y)

        current_position = board_bot.position
        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y,
        )
        return delta_x, delta_y