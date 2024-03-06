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
        # Calculate ditance between game objects
        return abs(board_bot.position.x - game.position.x) + abs(board_bot.position.y - game.position.y)
    
    def getNearestDiamonds(self, board_bot : GameObject, board : Board):
        # Retrieve the nearest diamond coordinate
        if board_bot.properties.diamonds == 4:
            array_diamond = [diamonds for diamonds in board.diamonds if diamonds.properties.points == 1]
            nearest = array_diamond[0]
            tot = self.getDistance(array_diamond[0], board_bot)
            for i in range(1, len(array_diamond)):
                if self.getDistance(array_diamond[i], board_bot) < tot:
                    tot = self.getDistance(array_diamond[i], board_bot)
                    nearest = array_diamond[i]
            return nearest
        else:
            array_diamond = [diamonds for diamonds in board.diamonds]
            nearest = array_diamond[0]
            tot = self.getDistance(array_diamond[0], board_bot)
            for i in range(1, len(array_diamond)):
                if self.getDistance(array_diamond[i], board_bot) < tot:
                    tot = self.getDistance(array_diamond[i], board_bot)
                    nearest = array_diamond[i]
            return nearest
    
    def getNearestTeleporter(self, board_bot : GameObject, board : Board):
        teleporter = []
        for i in board.game_objects:
            if i.type == "TeleportGameObject":
                teleporter.append(i)
        
    
    def getResetButton(self,board : Board):
        for i in board.game_objects:
            if i.type == "DiamondButtonGameObject":
                return i

    def next_move(self, board_bot : GameObject, board: Board):
        props = board_bot.properties
        current_position = board_bot.position
        # Analyze new state
        reset_coor = self.getResetButton(board)
        reset_distance = self.getDistance(reset_coor, board_bot)

        diamond_coor = self.getNearestDiamonds(board_bot, board)
        diamond_distance = self.getDistance(diamond_coor, board_bot)

        base_coor = board_bot.properties.base
        base_distance = abs(base_coor.x - board_bot.position.x) + abs(base_coor.y - board_bot.position.y)

        if props.diamonds == 5:
            # Move to base
            base = board_bot.properties.base
            self.goal_position = base
        elif props.diamonds == 0:
            if diamond_distance > reset_distance:
                self.goal_position = reset_coor.position
            else:
                self.goal_position = diamond_coor.position
        elif props.diamonds == 3:
            if diamond_distance > base_distance and reset_distance > base_distance:
                self.goal_position = base_coor
            else:
                self.goal_position = diamond_coor.position
        else:
            if reset_distance < diamond_distance:
                self.goal_position = reset_coor.position
            else:
                self.goal_position = diamond_coor.position

        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y,
        )
        return delta_x, delta_y