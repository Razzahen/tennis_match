from game import Game


class RegularGame(Game):
    """
    Represents a regular tennis game.
    """

    POINTS_MAPPING = {0: "0", 1: "15", 2: "30", 3: "40"}

    def __init__(self, players: list[str]):
        """
        Initialise a new regular tennis game.

        Args:
            players (list): List containing two player names as strings.
        """
        super().__init__(players)

    def has_finished(self):
        p1, p2 = self.players
        p1_points = self.points[p1]
        p2_points = self.points[p2]
        return (p1_points >= 4 or p2_points >= 4) and abs(p1_points - p2_points) >= 2

    def score(self) -> str:
        # Return the game score as a string.
        p1, p2 = self.players
        p1_points = self.points[p1]
        p2_points = self.points[p2]

        # If deuce or advantage
        if p1_points >= 3 and p2_points >= 3:
            if p1_points == p2_points:
                return "Deuce"
            elif p1_points == p2_points + 1:
                return f"Advantage {p1}"
            elif p2_points == p1_points + 1:
                return f"Advantage {p2}"
        # Otherwise, show the normal score.
        return f"{self.POINTS_MAPPING.get(p1_points, '40')}-{self.POINTS_MAPPING.get(p2_points, '40')}"
