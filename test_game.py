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
        
    def test_compare_tools_draw(self):
        tools = ['rock', 'paper', 'scissors']
        
        player_tool, comp_tool = "rock", "rock"
        player_score, comp_score = 2, 1
        result = g.compare_tools(player_tool, comp_tool, tools, comp_score, player_score)
        self.assertEqual((result), (2,1))
        
        player_tool, comp_tool = "paper", "paper"
        player_score, comp_score = 0, 0
        result = g.compare_tools(player_tool, comp_tool, tools, comp_score, player_score)
        self.assertEqual((result), (0,0))
        
        player_tool, comp_tool = "scissors", "scissors"
        player_score, comp_score = 5, 4
        result = g.compare_tools(player_tool, comp_tool, tools, comp_score, player_score)
        self.assertEqual((result), (5,4))
        
    
    def test_compare_tools_update_player_score(self):
        pass
    
    # def test_compare_tools(self):
    #     pass

if __name__ == '__main__':
    unittest.main()