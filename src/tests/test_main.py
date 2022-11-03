from main import main

game_keys = 'game, total_kills, players, kills'
matches_keys = 'front-end/src/dataJson/matches.json'


def test_that_all_key_elements_are_in_all_games():
  assert any(substring in game_keys for substring in matches_keys)
