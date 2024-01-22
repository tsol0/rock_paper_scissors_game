import unittest

import game as g


class TestGameFunctions(unittest.TestCase):
    
    def test_winner_found_false(self):
        player_score = 2
        comp_score = 1
        score_to_win = 5
        result = g.check_for_winner(player_score, comp_score, score_to_win)
        self.assertEqual(result, False)
    
    def test_check_for_winner_comp_win(self):
        player_score = 2
        comp_score = 3
        score_to_win = 3
        result = g.check_for_winner(player_score, comp_score, score_to_win)
        self.assertEqual(result, True)
        
    def test_check_for_winner_player_win(self):
        player_score = 3
        comp_score = 1
        score_to_win = 3
        result = g.check_for_winner(player_score, comp_score, score_to_win)
        self.assertEqual(result, True)
        

if __name__ == '__main__':
    unittest.main()