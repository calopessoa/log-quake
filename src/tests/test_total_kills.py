from src.helpers.total_kills import total_kills
from collections import Counter

mock_game_10 = {'game': 10, 'InitGame': 2355, 'ShutdownGame': 2526}

mock_player_score = {"Zeh": 7, "Isgalamido": 6, "Chessus": 5, "Dono da Bola": 3, "Assasinu Credi": 3, "Mal": 1, "Oootsimo": -1}

mock_penalties = {'Dono da Bola': -2, 'Oootsimo': -2, 'Mal': -5, 'Zeh': -2, 'Isgalamido': -4, 'Chessus': -1, 'Assasinu Credi': -2}

mock_killers = {'Oootsimo': 1, 'Dono da Bola': 5, 'Zeh': 9, 'Chessus': 6, 'Mal': 6, 'Assasinu Credi': 5, 'Isgalamido': 10}

def test_that_game_10_returns_the_count_of_60():
  assert total_kills(mock_game_10) == 60

def test_the_sum_of_all_player_and_world_kills_equals_to_60_in_game_10():
  penalties = dict(Counter(mock_penalties))
  for key, value in penalties.items():
    penalties[key] = abs(value)
  new_dictionary = {obj: penalties[obj] + mock_killers.get(obj, 0) for obj in penalties}
  assert sum(new_dictionary.values())