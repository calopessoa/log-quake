# from src.helpers.regex import *
kill_pattern = r"(?:^|\W)Kill(?:$|\W)"

import re

def total_kills(i):
  with open ('src/log/index.log', 'rt') as games_list:
    kills = 0
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        findKills = re.findall(kill_pattern, line)
        if findKills:
          kills += 1

    return kills

# print(total_kills({'game': 2, 'InitGame': 10, 'ShutdownGame': 97}))
