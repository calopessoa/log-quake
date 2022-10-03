import pytest
from src.helpers.game_number import game_number

mock_all_games = [{'game': 1, 'InitGame': 1, 'ShutdownGame': 10}, {'game': 2, 'InitGame': 10, 'ShutdownGame': 97}, {'game': 3, 'InitGame': 97, 'ShutdownGame': 158}, {'game': 4, 'InitGame': 158, 'ShutdownGame': 674}, {'game': 5, 'InitGame': 674, 'ShutdownGame': 816}, {'game': 6, 'InitGame': 816, 'ShutdownGame': 1012}, {'game': 7, 'InitGame': 1012, 'ShutdownGame': 1612}, {'game': 8, 'InitGame': 1612, 'ShutdownGame': 1991}, {'game': 9, 'InitGame': 1991, 'ShutdownGame': 2355}, {'game': 10, 'InitGame': 2355, 'ShutdownGame': 2526}, {'game': 11, 'InitGame': 2526, 'ShutdownGame': 2692}, {'game': 12, 'InitGame': 2692, 'ShutdownGame': 3406}, {'game': 13, 'InitGame': 3406, 'ShutdownGame': 3461}, {'game': 14, 'InitGame': 3461, 'ShutdownGame': 4015}, {'game': 15, 'InitGame': 4015, 'ShutdownGame': 4064}, {'game': 16, 'InitGame': 4064, 'ShutdownGame': 4093}, {'game': 17, 'InitGame': 4093, 'ShutdownGame': 4228}, {'game': 18, 'InitGame': 4228, 'ShutdownGame': 4296}, {'game': 19, 'InitGame': 4296, 'ShutdownGame': 4712}, {'game': 20, 'InitGame': 4712, 'ShutdownGame': 4758}, {'game': 21, 'InitGame': 4758, 'ShutdownGame': 5304}]

def test_game_number():
    'Returns the expected index for each game, whereas InitGame is the initial line and ShutdownGame is the final line of that match'
    assert game_number() == mock_all_games

def test_game_number_one():
    'Returns the expected index for each game, whereas InitGame is the initial line and ShutdownGame is the final line of that match'
    assert game_number()[0] == {'game': 1, 'InitGame': 1, 'ShutdownGame': 10}

def test_game_number_N():
    'Should not associate a given index with another game index output'
    assert game_number()[1] != mock_all_games[20]