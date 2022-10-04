from src.helpers.decrement_kills import decrement_kills
from src.helpers.player_kills import player_kills

mock_penalties = {'Dono da Bola': -2, 'Oootsimo': -2, 'Mal': -5, 'Zeh': -2, 'Isgalamido': -4, 'Chessus': -1, 'Assasinu Credi': -2}

mock_killers = {'Oootsimo': 1, 'Dono da Bola': 5, 'Zeh': 9, 'Chessus': 6, 'Mal': 6, 'Assasinu Credi': 5, 'Isgalamido': 10}

mock_game_10 = {'game': 10, 'InitGame': 2355, 'ShutdownGame': 2526}

mock_game_13 = {'game': 13, 'InitGame': 3406, 'ShutdownGame': 3461}

def test_that_game_10_returns_right_players_penalties():
  assert decrement_kills(mock_game_10) == mock_penalties

def test_same_players_in_score_and_possible_penalties():
  assert decrement_kills(mock_game_10).keys() == player_kills(mock_game_10).keys()

def test_all_penalties_are_negative_values():
  assert all(value < 0 for value in mock_penalties.values())

def test_that_player_Chessus_has_no_special_characters_in_penalties():
  assert 'Chessus!' not in decrement_kills(mock_game_13)