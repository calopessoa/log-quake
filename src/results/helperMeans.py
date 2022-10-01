import re
from collections import Counter

death_cause = r"((?<=by\s).*)"

def helperMeans(i):
  with open ('src/log/index.log', 'rt') as games_list:
    deaths = []
    new_kill_list = []
    for index, line in enumerate(games_list):
      if index >= i.get('InitGame') and index <= i.get('ShutdownGame'):
        find_kill = re.findall(death_cause, line)
        if find_kill:
          deaths.append(find_kill[0])
        # contará a incidência de cada elemento e as ordenará em uma lista
        kill_count = Counter(deaths).most_common()
        # irá remover cada incidência da palavra <world> e retornará um dict
        new_kill_list = dict([tup for tup in kill_count if tup[0] != '<world>'])

    return new_kill_list
