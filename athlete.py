# module to hold and mutate athlete data (players, coaches, etc.)

from enum import Enum

class PlayerPosition(Enum):
    FORWARD = "forward"
    MIDFIELDER = "midfielder"
    DEFENDER = "defender"
    GOALKEEPER = "goalKeeper"


class CoachRole(Enum):
    HEADCOACH = "headCoach"
    ASTCOACH = "astCoach"


class Athlete:
    def __init__(self, FName, LName, Number=None, Position=None):
        self.id = None
        self.FName = FName
        self.LName = LName
        self.Number = Number
        self.Position = Position


class Player(Athlete):
    def __init__(self, Number, Position):
        self.Number = Number
        self.Position = Position
