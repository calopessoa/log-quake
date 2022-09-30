import re
from collections import Counter
# from src.helpers.regex import *
killer = r"([^ ]+)(?=\skilled)"

def player_kills(i):
  with open ('src/log/index.log', 'rt') as games_list:
    players = []
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        find_player = re.findall(killer, line)
        if find_player:
          players.append(find_player[0])
        kill_count = Counter(players).most_common()
        new_kill_list = dict([tup for tup in kill_count if tup[0] != '<world>'])

    return new_kill_list
# print(player_kills({'game': 2, 'InitGame': 10, 'ShutdownGame': 97}))