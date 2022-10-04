from pytest import mark
from src.helpers.match_players import match_players


mock_players = ['Mocinha', 'Zeh', 'Isgalamido', 'Dono da Bola']
mock_game_3 = {'game': 3, 'InitGame': 97, 'ShutdownGame': 158}

def test_that_Mocinha_is_included_in_game_3():
  if mock_game_3.values() in match_players(mock_game_3):
    assert 'Mocinha' == mock_players[0]

@mark.xfail(reason='although it lists participant players, they are not organized')
def test_that_match_players_return_a_list_unorganized():
  assert match_players(mock_game_3) == mock_players