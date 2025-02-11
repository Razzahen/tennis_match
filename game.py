from abc import ABC, abstractmethod


class Game(ABC):
    """
    Abstract Game Interface
    """

    def __init__(self, players: list[str]):
        super().__init__()
        self.players = players
        self.points = {player: 0 for player in players}
        self.winner = None

    def point_won_by(self, player: str):
        """
        Record a point won by the specified player and check if the game has a winner.
        """
        # If the game already has a winner, raise an error
        if self.winner:
            raise ValueError("Game is over")

        self.points[player] += 1
        if self.has_finished():
            self.winner = player

    def has_started(self) -> bool:
        return any(points > 0 for points in self.points.values())

    @abstractmethod
    def has_finished(self) -> bool:
        """Implement game-specific winning logic"""
        pass

    @abstractmethod
    def score(self) -> str:
        """Implement game-specific scoring display"""
        pass
