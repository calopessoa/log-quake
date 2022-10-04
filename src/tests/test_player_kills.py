from pytest import mark
from src.helpers.player_kills import player_kills

mock_killers = {
  'Oootsimo': 1, 'Dono da Bola': 5, 'Zeh': 9, 'Chessus': 6, 'Mal': 6, 'Assasinu Credi': 5, 'Isgalamido': 10
  }

mock_game_10 = {'game': 10, 'InitGame': 2355, 'ShutdownGame': 2526}

mock_no_killers = {'Isgalamido': 0}

mock_game_0 = {'game': 1, 'InitGame': 1, 'ShutdownGame': 11}

mock_game_13 = {'game': 13, 'InitGame': 3406, 'ShutdownGame': 3461}

def test_that_game_10_returns_right_score_of_killers():
  assert player_kills(mock_game_10) == mock_killers

def test_that_Zeh_is_a_player_in_game_10():
  assert 'Zeh' in player_kills(mock_game_10)

def test_if_a_game_with_no_kills_returns_a_zero_value():
  assert player_kills(mock_game_0) == mock_no_killers

def test_that_player_Chessus_has_no_special_characters():
  assert 'Chessus!' not in player_kills(mock_game_13)