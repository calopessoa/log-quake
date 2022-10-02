import re
from collections import Counter
from src.helpers.regex import *

WORLD = 'world>'

def player_kills(i):
  with open ('src/log/index.log', 'rt') as games_list:
    players = []
    assassins = []
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        find_player = re.findall(players_pattern, line)
        if find_player and find_player[0] != 'Chessus!':
          players.append(find_player[0])
          new_players = dict.fromkeys(players, 0)

        find_player = re.findall(killer, line)
        if find_player and find_player[0] != WORLD:
          assassins.append(find_player[0])
        kill_count = dict(Counter(assassins).most_common())
    new_players.update(kill_count)

    return new_players
