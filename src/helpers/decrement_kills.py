import re
from collections import Counter
from src.helpers.regex import *

WORLD = 'world>'

# this function will force a player to lose 1 score everytime <world> kills them

def decrement_kills(i):
  with open('src/log/index.log', 'rt') as games_list:
    decrement_score = []
    match = {}
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        find_player = re.findall(killer, line)
        if find_player and find_player[0] == WORLD:
          pk = re.findall(player_killed, line)
          decrement_score.append(pk[0])
    for busted in decrement_score:
      if busted in match:
        match[busted] += 1
      else:
        match[busted] = 1
    final_decrement = dict(Counter(match))
    for key, value in final_decrement.items():
      final_decrement[key] = -abs(value)

    return final_decrement
