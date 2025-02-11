from game import Game


class TieBreakGame(Game):
    """
    Represents a tie-break game in tennis.
    """

    def __init__(self, players):
        """
        Initialise a new tie-break game.

        Args:
            players (list): List containing two player names as strings.
        """
        super().__init__(players)

    def has_finished(self):
        p1, p2 = self.players
        p1_points = self.points[p1]
        p2_points = self.points[p2]
        return (p1_points >= 7 or p2_points >= 7) and abs(p1_points - p2_points) >= 2

    def score(self) -> str:
        p1, p2 = self.players
        return f"{self.points[p1]}-{self.points[p2]}"
