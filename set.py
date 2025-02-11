from regular_game import RegularGame
from tiebreak_game import TieBreakGame


class Set:
    """
    Represents a single tennis set consisting of multiple games.

    The set tracks the set score and manages the transition between regular games
    and tie-break games when the score reaches 6-6. A set is won when a player wins
    6 games with a 2-game lead, or wins a tie-break.
    """

    def __init__(self, player1: str, player2: str):
        """
        Initialise a new tennis set.

        Args:
            player1 (str): Name of the first player
            player2 (str): Name of the second player
        """
        self.players = [player1, player2]
        self.set_score = {player1: 0, player2: 0}
        self.current_game = RegularGame(self.players)
        self.set_over = False

    def point_won_by(self, player: str):
        """
        Record a point won by the specified player.

        Updates the current game score and, if the game is won, updates the set score.
        Also handles the transition to a tie-break game if necessary.

        Args:
            player (str): Name of the player who won the point
        """
        if self.set_over:
            raise ValueError("Set is over")

        self.current_game.point_won_by(player)

        # Check if the game is over
        if self.current_game.has_finished():
            # A game has been won – update the set score.
            game_winner = self.current_game.winner
            self.set_score[game_winner] += 1

            # Check if the set is over.
            if self._is_set_over():
                self.set_over = True
                # Start of a new set
                self.current_game = RegularGame(self.players)
            else:
                # Decide whether the next game should be a tie-break.
                p1, p2 = self.players
                if self.set_score[p1] == 6 and self.set_score[p2] == 6:
                    self.current_game = TieBreakGame(self.players)
                else:
                    self.current_game = RegularGame(self.players)

    def _is_set_over(self) -> bool:
        """
        Check if the set is over.
        """
        p1, p2 = self.players
        p1_games = self.set_score[p1]
        p2_games = self.set_score[p2]
        # If the set score is 6-6, check if the tie-break has been won.
        if p1_games >= 6 or p2_games >= 6:
            if abs(p1_games - p2_games) >= 2:
                return True
            # Tie-break win leads to 7-6.
            if (p1_games == 7 and p2_games == 6) or (p2_games == 7 and p1_games == 6):
                return True
        return False

    def score(self) -> str:
        """
        Return the current score.
        """
        p1, p2 = self.players
        # When the set is over, only show the set score.
        if self.set_over:
            return f"{self.set_score[p1]}-{self.set_score[p2]}"
        # If the current game hasn't started (0-0), show just the set score.
        if not self.current_game.has_started():
            return f"{self.set_score[p1]}-{self.set_score[p2]}"
        return f"{self.set_score[p1]}-{self.set_score[p2]}, {self.current_game.score()}"
