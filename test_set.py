import unittest

from set import Set


class TennisTestCase(unittest.TestCase):
    def setUp(self):
        self.set = Set("player 1", "player 2")

    def test_game_scoring(self):
        # Test the scoring of a simple completed game
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

        self.assertEqual(self.set.score(), "1-0")
        self.assertFalse(self.set.set_over)
        self.assertEqual(self.set.current_game.score(), "0-0")

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
        self.assertEqual(self.set.current_game.score(), "0-0")

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

    def test_multiple_deuce_advantage_situations(self):
        """Test a game with multiple deuce and advantage situations"""
        # Get to deuce
        for _ in range(3):
            self.set.point_won_by("player 1")
            self.set.point_won_by("player 2")
        self.assertEqual(self.set.score(), "0-0, Deuce")

        # Advantage player 1, then back to deuce
        self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "0-0, Advantage player 1")
        self.set.point_won_by("player 2")
        self.assertEqual(self.set.score(), "0-0, Deuce")

        # Advantage player 2, then back to deuce
        self.set.point_won_by("player 2")
        self.assertEqual(self.set.score(), "0-0, Advantage player 2")
        self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "0-0, Deuce")

        # Finally player 1 wins with two consecutive points
        self.set.point_won_by("player 1")
        self.set.point_won_by("player 1")
        self.assertEqual(self.set.score(), "1-0")

    def test_long_tiebreak(self):
        """Test a longer tiebreak scenario with multiple lead changes"""
        # Get to 6-6
        for _ in range(6):
            for _ in range(4):
                self.set.point_won_by("player 1")
            for _ in range(4):
                self.set.point_won_by("player 2")

        # Now in tiebreak
        # Get to 6-6 in tiebreak
        for _ in range(6):
            self.set.point_won_by("player 1")
            self.set.point_won_by("player 2")

        # Player 1 gets to match point
        self.set.point_won_by("player 1")
        # Player 2 saves it
        self.set.point_won_by("player 2")
        # Player 2 gets match point
        self.set.point_won_by("player 2")
        # Player 1 saves it
        self.set.point_won_by("player 1")
        # Finally player 1 wins with two points
        self.set.point_won_by("player 1")
        self.set.point_won_by("player 1")

        self.assertEqual(self.set.score(), "7-6")
        self.assertTrue(self.set.set_over)

    def test_close_set_without_tiebreak(self):
        """Test a set that goes to 7-5"""
        # First 10 games split 5-5
        for _ in range(5):
            for _ in range(4):
                self.set.point_won_by("player 1")
            for _ in range(4):
                self.set.point_won_by("player 2")

        self.assertEqual(self.set.score(), "5-5")

        # Player 1 wins last two games
        for _ in range(8):
            self.set.point_won_by("player 1")

        self.assertEqual(self.set.score(), "7-5")
        self.assertTrue(self.set.set_over)

    def test_playing_after_set_over(self):
        """Test that we can't play points after the set is over"""
        # Win a quick set 6-0
        for _ in range(24):  # 6 games * 4 points
            self.set.point_won_by("player 1")

        self.assertTrue(self.set.set_over)

        # Try to play another point
        with self.assertRaises(ValueError):
            self.set.point_won_by("player 1")

    def test_invalid_player_name(self):
        """Test handling of invalid player names"""
        with self.assertRaises(KeyError):
            self.set.point_won_by("player 3")


# Main (if run as script)
if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
