from main import main

game_keys = 'game, total_kills, players, kills'

def test_that_21_matches_were_in_the_log():
  assert main().index('game', 1, 21)

def test_that_all_key_elements_are_in_all_games():
  assert any(substring in game_keys for substring in main())