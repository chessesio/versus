# module to hold and mutate match data including match results, player stats, and point score


class Points:
    def __init__(self):
        # points based on minutes played
        self._lt60 = 1
        self._gt60 = 1
        # points based on goal contributions
        self._scoreGK = 10
        self._scoreDef = 6
        self._scoreMid = 5
        self._scoreFwd = 4
        self._assist = 3
        # points based on clean sheet
        self._cleanSheetGK = 4
        self._cleanSheetDef = 4
        self._cleanSheetMid = 1
        self._per3ShotsSaved = 1
        # point bonus
        self._bonus = 3
        # point deductions (fouls and goal concensions)
        self._conceded2Goals = -1
        self._eachYellowCard = -1
        self._straightRed = -3
        self._eachOwnGoal = -2

    def scoreMinutesPlayed(self, param, multiplier):
        pass

    def scoreGoalContributions(self, param, multiplier):
        pass

    def scoreBonus(self, param, multiplier):
        pass

    def scoreDeductions(self, param, multiplier):
        pass


class Match(Points):
    def __init__(self):
        pass

    def score(self):
        pass
