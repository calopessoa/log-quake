import re
from src.helpers.regex import *

def match_players(i):
  with open ('src/log/index.log', 'rt') as games_list:
    players = []
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        find_player = re.findall(players_pattern, line)
        if find_player:
          players.append(find_player[0])

    return list(set(players))
