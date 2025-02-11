import unittest

from set import Set


class TennisTestCase(unittest.TestCase):
    def setUp(self):
        self.set = Set("player 1", "player 2")

    def test_game_scoring(self):
        # Given the example in the prompt:
        self.set.point_won_by("player 1")
        self.set.point_won_by("player 2")
        self.assertEqual(self.set.score(), "0-0, 15-15")

        self.set.point_won_by("player 1")
        self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "0-0, 40-15")

        self.set.point_won_by("player 2")
        self.set.point_won_by("player 2")
        self.assertEqual(self.set.score(), "0-0, Deuce")

        self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "0-0, Advantage player 1")

        self.set.point_won_by("player 1")
        # After winning the game, the set score becomes 1-0 and the game resets.
        self.assertEqual(self.set.score(), "1-0")

    def test_set_complete_without_tiebreak(self):
        # Simulate a set won 6-0 by player 1.
        # Each game is won by player 1 by scoring four straight points.
        for _ in range(5):  # first 5 games, player 1 wins
            for _ in range(4):
                self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "5-0")
        # Game 6:
        for _ in range(4):
            self.set.point_won_by("player 1")
        # Set should now be over.
        self.assertEqual(self.set.score(), "6-0")
        self.assertTrue(self.set.set_over)

    def test_set_complete_with_tiebreak(self):
        # Get to 6-6
        for _ in range(6):
            for _ in range(4):
                self.set.point_won_by("player 1")
            for _ in range(4):
                self.set.point_won_by("player 2")

        # Now we're at 6-6, verify the score
        self.assertEqual(self.set.score(), "6-6")
        self.assertFalse(self.set.set_over)

        # Win tiebreak 7-5
        for _ in range(6):
            self.set.point_won_by("player 1")
        for _ in range(5):
            self.set.point_won_by("player 2")

        # Player 1 wins tiebreak
        self.set.point_won_by("player 1")

        # Final set score should be 7-6
        self.assertEqual(self.set.score(), "7-6")
        self.assertTrue(self.set.set_over)


# ---------------------------
# Main (if run as script)
# ---------------------------
if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
