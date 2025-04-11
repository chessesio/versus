# module to hold and mutate athlete data (players, coaches, etc.)


class Player:
    def __init__(self, id, fName, lName, role, number=None, position=None):
        self._id = id
        self._fName = fName
        self._lName = lName
        self._role = role
        self._number = number
        self._position = position


    def addPlayer(self):
        pass
